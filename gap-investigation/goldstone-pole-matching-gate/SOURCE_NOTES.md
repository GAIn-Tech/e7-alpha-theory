# Primary-source check: curvature is not the pole

The sources were read from the retained primary PDFs, not inferred from abstracts. Their hashes are included in receipt.json. Original PDFs stay read-only in ../ir-resummed-vacuum-gate/sources/.

1. J. Elias-Miro, J. R. Espinosa, T. Konstandin, *Taming Infrared Divergences in the Effective Potential*, arXiv:1406.2652, https://arxiv.org/abs/1406.2652.
   - Printed page 3 (PDF page 4), section 2: terms G^2 log^m(G) are safe in V but divergent in V''. The source explicitly says V'' is the zero-external-momentum two-point function, while the pole is at p^2=M_h^2, and that the momentum correction has the same IR singularities which cancel in the result.
   - This passage contrasts that situation with G log^m(G) terms affecting the first derivative: stationarity has to be repaired within the potential. Thus a remaining curvature log is not evidence that unspecified hard two-loop terms must make V C2.
   - Printed page 23 (PDF page 24), Appendix A, equation (A.4): B(X,Y)=-integral_0^1 log([Xx+Y(1-x)-s x(1-x)]/Q^2) dx, with positive infinitesimal imaginary part in s. The calculation uses I=-B and exactly this branch. Equation (A.5) gives B(0,0)=2-log(-s/Q^2).
2. S. P. Martin, *Taming the Goldstone contributions to the effective potential*, arXiv:1406.2355, https://arxiv.org/abs/1406.2355.
   - Page 18, Outlook: the resummed minimization condition and potential value at its minimum are free of the problematic G dependence. For second-derivative mass approximations, the source says the ultimate resolution comes from full self-energy functions at nonzero external momentum.

**Consequence for the predecessor report:** its explicitly computed Gaussian radial log is a valid obstruction to an ordinary C2-potential argument. Its sentence suggesting hard two-loop terms should cancel or reorganize that curvature singularity should not be read as a requirement that hard two-loop matching removes it. Resummed stationarity and nonzero-momentum poles are different gates. This lane records the refinement additively, without editing the predecessor.

Machine-extracted relevant primary pages are retained in primary-source-excerpts.txt. These are the same source texts read during the investigation, not generated physics prose.
