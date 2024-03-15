import pandas as pd

#dont forget to write achive name is releated to the last upload
archive_name = '*.csv'
df = pd.read_csv(archive_name)

def clean_unnecessary_collumns(df,name):
  header = ["ID",'Penetration No.','Location','FRL','Ref', 'Is Active']
  df.to_csv(name+'.csv',columns= header)

def sort_by_location(df):
  new_df = df.sort_values(by=['ID'],ascending=False)
  new_df = new_df.sort_values(by=['Location'])
  return new_df

new_df = sort_by_location(df)
clean_unnecessary_collumns(new_df,"Martin place - level 06")