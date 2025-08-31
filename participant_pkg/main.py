import csv
from pathlib import Path
# from participant_pkg import load_participant, save_participant
import file_ops
workspace = Path("workspace")
csv_file = workspace / "contact.csv"
participant_dict = {}
while True:
  try:
      print("\n enter participant details")
      name = input("Enter Your Name:\t ")
      if not name.isalpha():
        raise ValueError("Invalid Input")
      else:
        participant_dict["name"] = name
      age = input("Enter Your Age: ")
      if not age.isdigit():
        raise ValueError("Invalid Input Please enter digit number")
      else:
        participant_dict["age"] = age
      phone = input("Enter Your Phone Number: ")
      if not phone.isdigit() and not len(phone) == 11:
        print("Ensure the phone number is digit and is 11 digit")
      else:
        participant_dict["phone_number"] = phone
        print("Correct")
        
      track = input("Enter Participant Track: ")
      if not track.isalpha():
        continue
      else:
        participant_dict["track"] = track

  except FileNotFoundError as e:
    print("Error during file operation:", e)
  print(participant_dict)
  file_ops.save_participant(csv_file, participant_dict)
# participant  = [["name", "age", "phone", "track"]]
  try:
    file_ops.save_participant(csv_file, participant_dict)
    
    file_ops.load_participants(csv_file)
    print("Participant saved successfully!\n")
    
  except Exception as e:
    print(f"Failed to save participant: {e}\n")
    print("Try again")
  more = input("Add another participant? (y/n): ").lower()
  if more != 'y':
            break

      # raise ValueError("Invalid Input")
