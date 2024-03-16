import pandas as pd

#dont forget to write achive name is releated to the last upload


def clean_unnecessary_collumns(df,name):
  header = ["ID",'Penetration No.','Location','FRL','Ref', 'Is Active']
  df.to_csv(name+'.csv',columns= header,index = False)

def sort_by_location(archive_name):
  df = archive_name
  df = df.sort_values(by=['ID'],ascending=False)
  df = df.sort_values(by=['Location'])
  return df
