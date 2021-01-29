import aoc

session_ids = {"Sebi" : "53616c7465645f5f65abe89ef3b2ac063a25e8be1597684d830da9abdcf516a07d72b3bd7a9b2e876091d34eff674e7a","Andor" : "53616c7465645f5fb8f81b08fcee602623f6f024e6513bb18b3e368905acffa50591108289df5e5cb7163f05abf90d68", "Artur": "53616c7465645f5f6d08127189bafcc6cd17d8668b41278b6413d795b5370bfa679654a47791818c33a66c880f97c763"}

for i in session_ids:
    aoc.set_session(session_ids[i])
    
    df = df = aoc.csillagok(2020)
    instance = aoc.get_spreadsheet_instance("aocprogprojekt-3efc6a57ec01.json")
    sheet = aoc.get_df(instance)
    sheet[i] = df
    aoc.update_spreadsheet(sheet, instance)

    
    
szumma = {}
for i in list(sheet.columns):
    szumma[i] = [sum(sheet[i])]
df = sheet.append(aoc.pd.DataFrame(szumma, index = ["összesen"]))   
aoc.to_pdf(df)
#utolsó sorban összeadtam a számokat és kiraktam egy pdf-be, aminek az a neve hogy current_standing.pdf

aoc.send_email_update("velkeyartur@gmail.com","lyprjyjfolhmqvqt","kbb1795@gmail.com","current_standing.pdf")