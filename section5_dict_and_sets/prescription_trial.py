from prescription_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# Remove Warfarin and add Edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    print(patient, prescription)
    try:
        prescription.remove(warfarin) # Because warfarin should not be used with other drugs
        prescription.add(edoxaban) # Because edoxaban has same effect with warfarin
    except KeyError:
        print(f"Patient {patient} is not taking Warfarin."
              f" Please remove {patient} from the trial")
    print(patient, prescription)
