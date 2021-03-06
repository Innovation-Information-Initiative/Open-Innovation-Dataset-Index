from fuzzywuzzy import fuzz
import pandas as pd

def match_schema_fields():
	data = pd.read_csv('index_archive/Open_Innovation_Datasets.csv', header=0)
	salient_fields = pd.read_csv('index_archive/Salient_Fields.csv', header=0)

	print(data.columns.values, salient_fields.columns.values)

	for index, row in data.iterrows():
		fields_list = str(row['schema_fields']).split(', ')
		suggestions = []
		for field_name in salient_fields['Name'].values:
			possibilities = []
			for field in fields_list:
				ratio = fuzz.ratio(field, field_name)
				if ratio > 60:
					possibilities.append({
						'field': field,
						'salient_field': field_name,
						'score': ratio
						})
			if len(possibilities) > 0:
				top_suggestion = sorted(possibilities, key=lambda poss: poss['score'])[0]
				suggestions.append(top_suggestion)
		if len(suggestions) > 0:
			print(row['title'], suggestions)

if __name__ == "__main__":
	match_schema_fields()