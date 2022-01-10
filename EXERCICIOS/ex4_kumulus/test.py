file_name = 'C:\\Users\\manoel.torres\\OneDrive - Kumulus\\Documents\\GitHub\\Python\\EXERCICIOS\\ex4_kumulus\\techcrunch (1).csv'

lines = (line for line in open(file_name))

list_line = (s.rstrip().split(",") for s in lines)

cols = next(list_line)

company_dicts = (dict(zip(cols, data)) for data in list_line)

funding = (

    int(company_dict["raisedAmt"])

    for company_dict in company_dicts

    if company_dict["round"] == "a"

)

total_series_a = sum(funding)

print(f"Total series A fundraising: ${total_series_a}")