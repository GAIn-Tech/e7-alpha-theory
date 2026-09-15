"""Scoped selective official-distribution installer, HTTP byte ranges."""
import io, json, struct, urllib.request, zipfile, time, concurrent.futures, hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
URL='https://github.com/leanprover/lean4/releases/download/v4.32.1/lean-4.32.1-windows.zip'
SIZE=832108412

def fetch(start,end):
 for attempt in range(6):
  try:
   with urllib.request.urlopen(urllib.request.Request(URL,headers={'Range':f'bytes={start}-{end}'}),timeout=90) as r:
    data=r.read()
    assert r.status==206 and len(data)==end-start+1,(r.status,len(data),end-start+1)
    return data
  except Exception:
   if attempt==5:raise
   time.sleep(2**attempt)

def catalog():
 tail=fetch(SIZE-65536,SIZE-1);idx=tail.rfind(b'PK\x05\x06');eocd=tail[idx:]
 _,_,_,_,count,cs,co,_=struct.unpack('<4s4H2LH',eocd[:22])
 central=fetch(co,co+cs-1)
 # A sparse local zip has the exact central-directory addresses but no bodies.
 path=P/'distribution-catalog.zip'
 with path.open('wb') as f:f.seek(co);f.write(central);f.write(eocd)
 with zipfile.ZipFile(path) as z: infos=z.infolist()
 return infos

def wanted(x):
 n=x.filename
 return (('/lib/lean/Init' in n and n.endswith(('.olean','.olean.private','.olean.server','.ir','.ilean'))) or n.endswith('/lib/lean/Init.olean') or n.endswith('/bin/lean.exe') or n.endswith('/bin/lake.exe') or ('/bin/' in n and n.endswith('.dll')))

def install_one(x):
 dest=P/'toolchain'/Path(x.filename).relative_to('lean-4.32.1-windows')
 if dest.exists() and dest.stat().st_size==x.file_size:return
 body=fetch(x.header_offset,x.header_offset+30+len(x.filename.encode())+len(x.extra)+x.compress_size+4096-1)
 stream=io.BytesIO(body)
 # Parse local header, not central extra, because these can differ.
 fields=struct.unpack('<4s5H3L2H',body[:30]);off=30+fields[-2]+fields[-1]
 compressed=body[off:off+x.compress_size]
 import zlib
 data=zlib.decompress(compressed,-15) if x.compress_type==8 else compressed
 assert len(data)==x.file_size and (zlib.crc32(data)&0xffffffff)==x.CRC
 dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
 return len(compressed)

if __name__=='__main__':
 import sys
 infos=catalog(); chosen=[x for x in infos if wanted(x)]
 print(json.dumps({'files':len(chosen),'compressed':sum(x.compress_size for x in chosen),'categories':{k:sum(x.compress_size for x in infos if k in x.filename) for k in ['/lib/lean/','/bin/','/lib/clang/']}}),flush=True)
 (P/'distribution_catalog.json').write_text(json.dumps([{'name':x.filename,'size':x.file_size,'compressed':x.compress_size} for x in chosen],indent=2))
 if '--install' in sys.argv:
  # Coalesce selected entries into fixed 2 MiB chunks; bounded parallel range fetch.
  block=2*1024*1024
  chunks=sorted({j for x in chosen for j in range(x.header_offset//block,(x.header_offset+30+len(x.filename.encode())+len(x.extra)+x.compress_size+4096)//block+1)})
  cache=P/'download-parts';cache.mkdir(exist_ok=True)
  def get_chunk(j):
   dest=cache/str(j);start=j*block;end=min(SIZE-1,start+block-1)
   if not dest.exists() or dest.stat().st_size!=end-start+1:dest.write_bytes(fetch(start,end))
   return j
  with concurrent.futures.ThreadPoolExecutor(max_workers=32) as pool:
   for i,j in enumerate(pool.map(get_chunk,chunks)):
    if i%10==0:print('downloaded',i,'of',len(chunks),flush=True)
  sparse=P/'distribution-catalog.zip'
  with sparse.open('r+b') as out:
   for j in chunks:out.seek(j*block);out.write((cache/str(j)).read_bytes())
  with zipfile.ZipFile(sparse) as archive:
   for x in chosen:
    dest=P/'toolchain'/Path(x.filename).relative_to('lean-4.32.1-windows')
    dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(archive.read(x))
  print('INSTALL_COMPLETE',flush=True)
