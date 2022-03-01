// UUID generation based on a script by Carlos Perez, clayperez@gmail.com
//
// REFERENCES:
// https://developers.google.com/apps-script/guides/triggers/events
// https://www.fiznool.com/blog/2014/11/16/short-id-generation-in-javascript/

const SHEETS = [
  {
    sheet_name: "Open_Innovation_Datasets",
    uuid_col: 1,
    timestamp_col: 26,
    location_col: 4,
    author_col: 6,
    desc_col: 5,
    cit_col: 7,
  },
  {
    sheet_name: "Innovation_Data_Toolkit",
    uuid_col: 1,
    timestamp_col: 13
  }
]

function generateUID () {
  return Utilities.getUuid();
}

function addMetadata(sheet, range, sheet_cols) {
  var rangeValues = range.getValues();

  rangeValues.forEach(function(row,index,arr){
    var contents = row.join("").length;

    if(contents > 0) { // verify row not empty

      // generate UUID if not one already
      var idRange = sheet.getRange( range.getRow() + index, sheet_cols.uuid_col ); 
      var idCell = idRange.getCell( 1, 1 );
      var idValue = idCell.getValue();
      if (idValue == "") {
        idCell.setValue( generateUID() );
      }

      // fetch citation if there's space for one
      if('cit_col' in sheet_cols) {
        console.log('fetching citation')
      }

      // finally, update the timestamp
      var d = new Date();
      var timeStamp = d.toUTCString();

      var timeRange = sheet.getRange( range.getRow() + index, sheet_cols.timestamp_col );
      var editCell = timeRange.getCell( 1, 1 );
      if(range.getRow() !== 1){
        editCell.setValue(timeStamp);
       } 
    }
  });
  
}

function onEdit(evt) {
  const range = evt.range;
  const sheet = range.getSheet();
  
  // check if it's a sheet we're doing anything to
  if (SHEETS.filter(e => e.sheet_name === sheet.getSheetName()).length === 0){
    return;
  }
  else {
    const sheet_cols = SHEETS.filter(e => e.sheet_name === sheet.getSheetName())[0];
    addMetadata(sheet, range, sheet_cols);
  }

}
