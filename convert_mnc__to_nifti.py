import nibabel as nib

# Load the MINC file (decompressed .mnc version)
img = nib.load("t1_icbm_normal_1mm_pn3_rf20.mnc")

# Save to NIfTI format
nib.save(img, "t1_icbm_normal_1mm_pn3_rf20.nii.gz")

print("Conversion successful.")
