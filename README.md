# Tissue-Bones-Medical-Image-Visualization
The goal of this code is using Python to Read DICOM (Digital Imaging and Communications in Medicine) files and generate JPEG images based on hounsfield units windows for better visualization of bones or tissue.

The DICOM CT (Computed Tomography) files were https://www.dicomlibrary.com/ 

The windowing process was experimental, since i have no sufficient expertise about this process. Although, the **HU** Values ware based on **A Hounsfield value-based approach for automatic recognition of brain haemorrhage**: https://doi.org/10.1080/24751839.2018.1547951.

After the windowing process the images were submited to bicubic interpolation (the most usual interpolation method according to Oleg S. Pianykh at **Digital Imaging and Communications in Medicine (DICOM): A Practical Introduction and Survival Guide**) to achieve the desired dimensions.
