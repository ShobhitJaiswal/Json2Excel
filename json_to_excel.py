import pandas as pd

print ("Note: input file is in same directory")

try:
    input_filename=input("Enter json file name: ")
    print ("Input file is %s" %input_filename)

    destination_filename=input("Enter output excel file name: ")
    print ("Output file is %s" %destination_filename)

    print ("Reading Inputs...")
    data_frame=pd.read_json(input_filename)

    print ("Creating Excel...")

    data_frame.to_excel(destination_filename)

    print ("Excel Creation Completed. Kindly Check")

except KeyboardInterrupt:
    print (" \n please specify input or output filename.") 
except Exception as e:
    print (e)