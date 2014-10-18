from wrangler import dw
import sys

if(len(sys.argv) < 3):
	sys.exit('Error: Please include an input and output file.  Example python script.py input.csv output.csv')

w = dw.DataWrangler()

# Split  repeatedly on '-'  into  rows
w.add(dw.Split(column=[],
               table=0,
               status="active",
               drop=True,
               result="row",
               update=False,
               insert_position="right",
               row=None,
               on="-",
               before=None,
               after=None,
               ignore_between=None,
               which=1,
               max="0",
               positions=None,
               quote_character=None))

# Delete rows 1,2,3,4,5,6,7,8,18
w.add(dw.Filter(column=[],
                table=0,
                status="active",
                drop=False,
                row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.RowIndex(column=[],
                  table=0,
                  status="active",
                  drop=False,
                  indices=[0,1,2,3,4,5,6,7,17])])))

# Edit data row 10  to ' |{{fb|TCH}}|align=center|{{sort dash}} |2 ([[1934 FIFA World Cup|1934]], [[1962 FIFA World Cup|1962]])|align=center|{{sort dash}}|align=center|{{sort dash}}|2||2||2| '
w.add(dw.Edit(column=["data"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.RowIndex(column=[],
                  table=0,
                  status="active",
                  drop=False,
                  indices=[9])]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="|{{fb|TCH}}|align=center|{{sort dash}} |2 ([[1934 FIFA World Cup|1934]], [[1962 FIFA World Cup|1962]])|align=center|{{sort dash}}|align=center|{{sort dash}}|2||2||2|",
              update_method=None))

# Cut from data between '|' and '{ any word '
w.add(dw.Cut(column=["data"],
             table=0,
             status="active",
             drop=False,
             result="column",
             update=True,
             insert_position="right",
             row=None,
             on=".*",
             before="{[a-zA-Z]+",
             after="\\|",
             ignore_between=None,
             which=1,
             max=1,
             positions=None))

# Split data repeatedly on '(align=center)||\d{1} '
w.add(dw.Split(column=["data"],
               table=0,
               status="active",
               drop=True,
               result="column",
               update=False,
               insert_position="right",
               row=None,
               on="(align=center)|\\|\\d{1} ",
               before=None,
               after=None,
               ignore_between=None,
               which=1,
               max="0",
               positions=None,
               quote_character=None))

# Fold   using  header as a key
w.add(dw.Fold(column=[],
              table=0,
              status="active",
              drop=False,
              keys=[-1]))

# Split value repeatedly on ', '  into  rows
w.add(dw.Split(column=["value"],
               table=0,
               status="active",
               drop=True,
               result="row",
               update=False,
               insert_position="right",
               row=None,
               on=", ",
               before=None,
               after=None,
               ignore_between=None,
               which=1,
               max="0",
               positions=None,
               quote_character=None))

# Merge   with glue  -
w.add(dw.Merge(column=[],
               table=0,
               status="active",
               drop=False,
               result="column",
               update=False,
               insert_position="right",
               row=None,
               glue="-"))

# Extract from merge on 'd{4}' between '|' and ']]'
w.add(dw.Extract(column=["merge"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on="\\d{4}",
                 before="]]",
                 after="\\|",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Extract from merge between ' any lowercase word ' and '-'
w.add(dw.Extract(column=["merge"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before="-",
                 after="[a-z]+",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Extract from merge on '[A-Z]{3}' between ' any word |' and '}'
w.add(dw.Extract(column=["merge"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on="[A-Z]{3}",
                 before="}",
                 after="[a-zA-Z]+\\|",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Drop fold
w.add(dw.Drop(column=["fold"],
              table=0,
              status="active",
              drop=True))

# Drop value
w.add(dw.Drop(column=["value"],
              table=0,
              status="active",
              drop=True))

# Drop merge
w.add(dw.Drop(column=["merge"],
              table=0,
              status="active",
              drop=True))

# Fill extract2  with values from above
w.add(dw.Fill(column=["extract2"],
              table=0,
              status="active",
              drop=False,
              direction="down",
              method="copy",
              row=None))

# Delete  rows where extract is null
w.add(dw.Filter(column=[],
                table=0,
                status="active",
                drop=False,
                row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.IsNull(column=[],
                table=0,
                status="active",
                drop=False,
                lcol="extract",
                value=None,
                op_str="is null")])))

w.apply_to_file(sys.argv[1]).print_csv(sys.argv[2])

