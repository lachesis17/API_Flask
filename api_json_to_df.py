import pandas as pd
import requests
import os
import sys
sys.stdout.reconfigure(encoding='utf-8') # So the output can print the unicode characters in the JSON

def main():
    def get_json_from_api(url: str, excel: bool) -> dict:
        dict_of_dfs = {} # dictionary to store the JSON response keys as dataframes

        try:
            req = requests.get(url) # GET request for some dummy JSON data from the API, use 'auth' and 'verify' args for authentication if needed
        except Exception as e:
            print(f'Bad request. {e}')
            return
        
        # Check the REST API response code
        if str(req.status_code).startswith("1"):
            return print(f'Informational data: {req.status_code}')
        if str(req.status_code).startswith("2"):
            print(f'Response OK: {req.status_code}')
        if str(req.status_code).startswith("3"):
            return print(f'Redirection, check the API url: {req.status_code}')
        if str(req.status_code).startswith("4"):
            return print(f'Bad Request: {req.status_code}')
        if str(req.status_code).startswith("5"):
            return print(f'ERROR: {req.status_code}')

        '''df = pd.json_normalize(req.json(), "users")  # To explicity request specific keys'''

        for key in req.json().keys(): # need the .json() method on the request so it doesn't just return its response code
            try:
                df = pd.json_normalize(req.json(), record_path=key) # Turn the JSON key into a dataframe
                dict_of_dfs[f'{key}'] = df # Add each key (dataframe) to the dictionary
            except TypeError as e:
                #print(e)
                pass

        if excel:
            json_dfs_to_excel(dict_of_dfs) # put the dict of dfs into excel

        return dict_of_dfs
    
    def json_dfs_to_excel(data: dict):
        dict_of_dfs = data

        if not len(dict_of_dfs.keys()) < 1: # write the first key to excel - writer can only 'append' sheets on an existing excel file, so create one
            next(iter(dict_of_dfs.values())).to_excel(f"{os.getcwd()}\json_response.xlsx", sheet_name=(f"{next(iter(dict_of_dfs))}"), index=None, index_label=None)
            writer = pd.ExcelWriter(f"{os.getcwd()}\json_response.xlsx", engine="openpyxl", mode="a", if_sheet_exists="replace")
        else:
            print(f"All returned JSON keys are empty.")
            return

        for (k,v) in dict_of_dfs.items():
            print(f"Saving {k} ...")
            v.to_excel(writer, sheet_name=(f"{str(k)}"), index=None, index_label=None)
        writer.close()

        print(f"JSON API response saved as Excel: {os.getcwd()}\json_response.xlsx")


    get_json_from_api(url='https://dummyjson.com/users', excel=True) # Run the GET request

if __name__ == "__main__":
    main()