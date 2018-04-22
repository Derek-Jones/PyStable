
This is an adaptation of libstable by Javier Royuela del Val (see README for details)
that creates a Python interface for use in SciPy.

A segmentation fault happens in: stable_integration_QAG2,
ie, inside call of gsl_integration_qag

When this problem is fixed, the assignment:
dist.stable_pdf_point=stable_pdf_point_LEVY;
in stable_pdf.c should be removed.

