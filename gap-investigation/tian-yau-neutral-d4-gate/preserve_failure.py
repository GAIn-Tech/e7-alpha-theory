"""Reconstruct initial executed source from the preserved pre-release snapshot.
This is explicitly reconstructed evidence, not a contemporaneous process dump.
"""
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent
text=(P/'verify-pre-release-snapshot.py').read_text()
start=text.index('\ndef wrong_end(v):');end=text.index('\ndef calculate():',start)
text=text[:start]+text[end:]
start=text.index('  # Produce admissible, character-preserving exact perturbations')
end=text.index('  for eta in etas:',start)
text=text[:start]+'''  for key in vs[0]:
   eta=c.hc({key:c.F(1)})
   if eta and c.dv(eta):etas.append(eta)
'''+text[end:]
start=text.index('  badend=c.add(wrong_end(vs[0]),c.dv(vs[1]))')
end=text.index('  # Full survivors are data',start)
text=text[:start]+text[end:]
start=text.index(' # Vertical-exact target representatives from the actual Koszul k=1 basis.')
end=text.index(' # Strong keywise,',start)
text=text[:start]+text[end:]
assert len(text.encode())==8170
lines=text.splitlines()
assert lines[90]==" assert counts['source_boundary']>0 and counts['target_d1_boundary']>0"
with (P/'failed-run-source-reconstructed.py').open('x',newline='\n') as h:h.write(text)
evidence={
 'failed_process':'proc_34c5ee2e337f','failed_exit_code':1,'failed_uptime_seconds':657,
 'source_snapshot_type':'Reconstructed by reversing recorded source patches; no contemporaneous source hash existed for this failed process.',
 'initial_source_bytes':len(text.encode()),'reconstructed_initial_sha256':hashlib.sha256(text.encode()).hexdigest(),
 'actual_failing_line_number':91,'actual_failing_line':lines[90],
 'cause':'hc vanishes on normalized harmonic lifts; attempted source-boundary test generated no perturbations, so source_boundary count was zero. A direct separate run of this initial source also failed at that same assertion with correct source text.',
 'stale_traceback_explanation':'The running process loaded its code before on-disk edits. Traceback rendering read later file lines, so displayed line122 rank assertion was not executed at that location.',
 'repair':'Generate explicit admissible character-preserving Laurent perturbations outside the harmonic support, apply hc, and require eta and dv(eta) nonzero. Check all four changed source total cocycles. Do not drop the source-boundary assertion.',
 'fresh_calculate_exit_code':0,
 'fresh_controls':{'source_boundary':4,'target_vertical_boundary':6,'target_d1_boundary':64,'wrong_curvature':4,'wrong_primitive_sign':10,'nilpotence_keys':6470,'cech_contraction_keys':6470,'wrong_End_sign':4},
 'scientific_result_origin':'compute.py independently assembled all four columns from actual chain endpoints before release verifier controls. All four raw endpoints were empty after exact accumulation; derived matrix rank was zero. The later equality assertion is an independent consistency check, not an assignment of endpoints.',
 'receipt_state_at_snapshot':'Neither receipt.json nor d4-chains.json existed; no release receipt was overwritten.',
 'further_negative_control_lesson':'Consistently flipping both supercommutator right-action signs can preserve its square. Detect this convention mutation against the actual fixed first-lift equation, not nilpotence alone.'}
with (P/'failed-run-evidence.json').open('x',newline='\n') as h:h.write(json.dumps(evidence,sort_keys=True,indent=2)+'\n')
print(json.dumps(evidence,indent=2))
