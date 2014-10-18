from wrangler import dw
import sys

if(len(sys.argv) < 3):
	sys.exit('Error: Please include an input and output file.  Example python script.py input.csv output.csv')

w = dw.DataWrangler()

# Split data repeatedly on newline  into  rows
w.add(dw.Split(column=["data"],
               table=0,
               status="active",
               drop=True,
               result="row",
               update=False,
               insert_position="right",
               row=None,
               on="\n",
               before=None,
               after=None,
               ignore_between=None,
               which=1,
               max=0,
               positions=None,
               quote_character=None))

# Delete empty rows
w.add(dw.Filter(column=[],
                table=0,
                status="active",
                drop=False,
                row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Empty(column=[],
               table=0,
               status="active",
               drop=False,
               percent_valid=0,
               num_valid=0)])))

# Extract from data after ' any word   '
w.add(dw.Extract(column=["data"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before=None,
                 after="[a-zA-Z]+  ",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Extract from data before '  '
w.add(dw.Extract(column=["data"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before="  ",
                 after=None,
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Extract from data on ' any number : any number  any lowercase word  -  any number : any number  any word '
w.add(dw.Extract(column=["data"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on="\\d+:\\d+[a-z]+ - \\d+:\\d+[a-zA-Z]+",
                 before=None,
                 after=None,
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Extract from data before '  any number :'
w.add(dw.Extract(column=["data"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before=" \\d+:",
                 after=None,
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Extract from data between 'Waitlist: ' and ')'
w.add(dw.Extract(column=["data"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before="\\)",
                 after="Waitlist: ",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Extract from data between 'Open: ' and ','
w.add(dw.Extract(column=["data"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before=",",
                 after="Open: ",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Extract from data between ': ' and ','
w.add(dw.Extract(column=["data"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before=",",
                 after=": ",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Extract from data on '[a-z.:A-Z]+ [a-z.:A-Z]+'
w.add(dw.Extract(column=["data"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on="[a-z.:A-Z]+ [a-z.:A-Z]+",
                 before=None,
                 after=None,
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Extract from data on '{begin} any number '
w.add(dw.Extract(column=["data"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on="^\\d+",
                 before=None,
                 after=None,
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Extract from data on 'CMSC any number '
w.add(dw.Extract(column=["data"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on="CMSC\\d+",
                 before=None,
                 after=None,
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Drop data
w.add(dw.Drop(column=["data"],
              table=0,
              status="active",
              drop=True))

# Fill extract9  with values from above
w.add(dw.Fill(column=["extract9"],
              table=0,
              status="active",
              drop=False,
              direction="down",
              method="copy",
              row=None))

# Delete  rows where extract8 is null and extract7 is null ...
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
                lcol="extract8",
                value=None,
                op_str="is null"),dw.IsNull(column=[],
                table=0,
                status="active",
                drop=False,
                lcol="extract7",
                value=None,
                op_str="is null"),dw.IsNull(column=[],
                table=0,
                status="active",
                drop=False,
                lcol="extract6",
                value=None,
                op_str="is null"),dw.IsNull(column=[],
                table=0,
                status="active",
                drop=False,
                lcol="extract5",
                value=None,
                op_str="is null"),dw.IsNull(column=[],
                table=0,
                status="active",
                drop=False,
                lcol="extract4",
                value=None,
                op_str="is null"),dw.IsNull(column=[],
                table=0,
                status="active",
                drop=False,
                lcol="extract3",
                value=None,
                op_str="is null"),dw.IsNull(column=[],
                table=0,
                status="active",
                drop=False,
                lcol="extract2",
                value=None,
                op_str="is null"),dw.IsNull(column=[],
                table=0,
                status="active",
                drop=False,
                lcol="extract1",
                value=None,
                op_str="is null"),dw.IsNull(column=[],
                table=0,
                status="active",
                drop=False,
                lcol="extract",
                value=None,
                op_str="is null")])))

# Fill extract8  with values from above
w.add(dw.Fill(column=["extract8"],
              table=0,
              status="active",
              drop=False,
              direction="down",
              method="copy",
              row=None))

# Delete  every 5 rows 
w.add(dw.Filter(column=[],
                table=0,
                status="active",
                drop=False,
                row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.RowCycle(column=[],
                  table=0,
                  status="active",
                  drop=False,
                  cycle=5,
                  start=0,
                  end=None)])))

# Fill extract7  with values from above
w.add(dw.Fill(column=["extract7"],
              table=0,
              status="active",
              drop=False,
              direction="down",
              method="copy",
              row=None))

# Delete  every 4 rows 
w.add(dw.Filter(column=[],
                table=0,
                status="active",
                drop=False,
                row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.RowCycle(column=[],
                  table=0,
                  status="active",
                  drop=False,
                  cycle=4,
                  start=0,
                  end=None)])))

# Fill extract6  with values from above
w.add(dw.Fill(column=["extract6"],
              table=0,
              status="active",
              drop=False,
              direction="down",
              method="copy",
              row=None))

# Fill extract5  with values from above
w.add(dw.Fill(column=["extract5"],
              table=0,
              status="active",
              drop=False,
              direction="down",
              method="copy",
              row=None))

# Fill extract4  with values from above
w.add(dw.Fill(column=["extract4"],
              table=0,
              status="active",
              drop=False,
              direction="down",
              method="copy",
              row=None))

# Delete  every 3 rows 
w.add(dw.Filter(column=[],
                table=0,
                status="active",
                drop=False,
                row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.RowCycle(column=[],
                  table=0,
                  status="active",
                  drop=False,
                  cycle=3,
                  start=0,
                  end=None)])))

# Fill extract3  with values from above
w.add(dw.Fill(column=["extract3"],
              table=0,
              status="active",
              drop=False,
              direction="down",
              method="copy",
              row=None))

# Fill extract2  with values from above
w.add(dw.Fill(column=["extract2"],
              table=0,
              status="active",
              drop=False,
              direction="down",
              method="copy",
              row=None))

# Delete  every 2 rows 
w.add(dw.Filter(column=[],
                table=0,
                status="active",
                drop=False,
                row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.RowCycle(column=[],
                  table=0,
                  status="active",
                  drop=False,
                  cycle=2,
                  start=0,
                  end=None)])))

w.apply_to_file(sys.argv[1]).print_csv(sys.argv[2])

