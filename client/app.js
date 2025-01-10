function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getBedValue() {
  var uiBedr = document.getElementsByName("uiBedr");
  for(var i in uiBedr) {
    if(uiBedr[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getYesNoValue() {
  var dropdown = document.getElementById("uipark").value; // Get the dropdown element
  
  if (dropdown === "yes") {
    return 1; // Return 1 for "Yes"
  } else if (dropdown === "no") {
    return 0; // Return 0 for "No"
  }
  return -1; // Return -1 if the value is invalid (optional)
}

function util() {
  var u = document.getElementById("uiutil").value;

  if (u=="all public facilities") {
    return "allpub"
  } else if (u=="all public facilities and electic operated lift") {
    return "elo"
  } else if (u=="no sewage") {
    return "nosewr"
  }
  return -1
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var sqft = document.getElementById("uiSqft");
  var age=document.getElementById("yrs");
  var bathrooms = getBathValue();
  var bedrooms=getBedValue();
  var room=document.getElementById("uiroom");
  var location = document.getElementById("uiLocations");
  var park=getYesNoValue();
  var sale_cond=document.getElementById("uisale");
  var mzzone=document.getElementById("uizone");
  var util_avail=util();
  var buildtype=document.getElementById("uibtype");
  var street=document.getElementById("uistreet")
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      area: location.value,
      sale_cond:sale_cond.value,
      park_facil:park,
      utility_avail:util_avail,
      buildtype:buildtype.value,
      street:street.value,
      mzzone:mzzone.value,
      property_age:age.value,
      int_sqft: sqft.value,
      n_bedroom:bedrooms,
      n_bathroom: bathrooms,
      n_room: room.value
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>Rs " + data.estimated_price.toString() + " </h2>";
      console.log(status);
  });
}

// function onPageLoad() {
//   console.log( "document loaded" );
//   var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
//   //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
//   $.get(url,function(data, status) {
//       console.log("got response for get_location_names request");
//       if(data) {
//           var locations = data.locations;
//           var uiLocations = document.getElementById("uiLocations");
//           $('#uiLocations').empty();
//           for(var i in locations) {
//               var opt = new Option(locations[i]);
//               $('#uiLocations').append(opt);
//           }
//       }
//   });
// }

// window.onload = onPageLoad;
