// AUTO GENERATE SIMPLE UNIQUE ID'S FOR NON-EMPTY ROWS
//
// Based on a script by Carlos Perez, clayperez@gmail.com
//
// REFERENCES:
// https://developers.google.com/apps-script/guides/triggers/events
// https://www.fiznool.com/blog/2014/11/16/short-id-generation-in-javascript/

var SHEETNAMES = ["Open_Innovation_Datasets", "Innovation_Data_Toolkit"] // change names!
var ID_COLUMN = 1;
var ID_LENGTH = 10;
var TIMESTAMP_COL;

// Thanks to Tom Spencer for this function
// Tom's website/blog is at fiznool.com
function generateUID () {
  return Utilities.getUuid();
}

function onEdit(evt) {
  var range = evt.range;
  var sheet = range.getSheet();
  console.log(sheet.getSheetName())
  if(!SHEETNAMES.includes(sheet.getSheetName()) ) return;
  if(sheet.getSheetName() === "Open_Innovation_Datasets") TIMESTAMP_COL = 22 // change name and timestamp cols!
  if(sheet.getSheetName() === "Innovation_Data_Toolkit") TIMESTAMP_COL = 14
  var rangeValues = range.getValues();

  rangeValues.forEach(function(row,index,arr){
    var conc = row.join("").length;
    if(conc > 0) { // The current row edited is NOT empty. Proceed.
      var idRange = sheet.getRange( range.getRow() + index, ID_COLUMN ); 
      var idCell = idRange.getCell( 1, 1 );
      var idValue = idCell.getValue();
      if (idValue == "") {
        idCell.setValue( generateUID() );
      }

      var d = new Date();
      var timeStamp = d.toUTCString();

      var timeRange = sheet.getRange( range.getRow() + index, TIMESTAMP_COL );
      var editCell = timeRange.getCell( 1, 1 );
      var editVal = editCell.getValue();
      if(editVal !== "Last Edit"){
        editCell.setValue(timeStamp);
       } 
    }
  });
  
}
