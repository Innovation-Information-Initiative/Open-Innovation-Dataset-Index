// AUTO GENERATE SIMPLE UNIQUE ID'S FOR NON-EMPTY ROWS
//
// Based on a script by Carlos Perez, clayperez@gmail.com
//
// REFERENCES:
// https://developers.google.com/apps-script/guides/triggers/events
// https://www.fiznool.com/blog/2014/11/16/short-id-generation-in-javascript/

var SHEETNAMES = ["Open_Innovation_Datasets", "Innovation_Data_Toolkit"]
var ID_COLUMN = 1;
var ID_LENGTH = 10;
var EDIT_COL;

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
  if(sheet.getSheetName() === "Open_Innovation_Datasets") EDIT_COL = 22
  if(sheet.getSheetName() === "Innovation_Data_Toolkit") EDIT_COL = 14
  // getValues()
  // as cells: [[A1,B1,C1],[A2,B2,C2],[A3,B3,C3],[A4,B4,C4],[...]]
  // as locals: [[11,21,31],[12,22,32],[13,23,33],[14,24,34],[...]]
  var rangeValues = range.getValues();

  // Loop over each row of the range and check for data being entered.
  // We don't want to commit a UID value to the ID column if the data
  // in adjacent columns was just deleted. We only want a UID for rows
  // with data in them.

  rangeValues.forEach(function(row,index,arr){
    var conc = row.join("").length; // Where we check for data in the row
    if(conc > 0) { // The current row edited is NOT empty. Proceed.
      var idRange = sheet.getRange( range.getRow() + index, ID_COLUMN ); // This is a 1-dimensional range that contains the ID cell we want to populate
      var idCell = idRange.getCell( 1, 1 );
      var idValue = idCell.getValue();
      if (idValue == "") {
        idCell.setValue( generateUID() );
      }

      var d = new Date();
      var timeStamp = d.toUTCString();

      var timeRange = sheet.getRange( range.getRow() + index, EDIT_COL );
      var editCell = timeRange.getCell( 1, 1 );
      var editVal = editCell.getValue();
      if(editVal !== "Last Edit"){
        editCell.setValue(timeStamp);
       } 
    }
  });
  
}
