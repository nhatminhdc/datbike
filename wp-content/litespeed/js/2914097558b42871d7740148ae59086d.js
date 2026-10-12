(function($){'use strict';$(document).ready(function(){const locationData=storeLocatorData;const jsonData=JSON.stringify(locationData);const provinces=[...new Set(locationData.map(location=>location.province))];let districts=[];const goongMapsApiKey=storeLocatorGoongData.maptiles_key;const default_lat=parseFloat(storeLocatorGoongData.default_lat);const default_lng=parseFloat(storeLocatorGoongData.default_lng);const default_zoom=parseInt(storeLocatorGoongData.zoom);const title_directions=storeLocatorGoongData.title_directions;let map;let markers=[];let currentLocationMarker=null;let filteredLocations=[...locationData];let userLocation=null;$(document).ready(function(){goongjs.accessToken=goongMapsApiKey;map=new goongjs.Map({container:'map',style:'https://tiles.goong.io/assets/goong_map_web.json',center:[default_lng,default_lat],zoom:default_zoom});populateProvinces();$('#provinceSelect').on('change',function(){populateDistricts($(this).val())});$('#searchBtn').on('click',function(){searchLocations()});$('#getCurrentLocation').on('click',function(){getUserLocation()});updateLocationsList(locationData);updateMap(locationData)});function populateProvinces(){provinces.forEach(province=>{$('#provinceSelect').append(`<option value="${province}">${province}</option>`)})}
function populateDistricts(selectedProvince){$('#districtSelect').html('<option value="">Quận/ Huyện</option>');if(!selectedProvince)return;const provinceDistricts=[...new Set(locationData.filter(location=>location.province===selectedProvince).map(location=>location.district))];provinceDistricts.forEach(district=>{$('#districtSelect').append(`<option value="${district}">${district}</option>`)})}
function searchLocations(){const searchAddress=$('#searchAddress').val().toLowerCase();const selectedProvince=$('#provinceSelect').val();const selectedDistrict=$('#districtSelect').val();filteredLocations=locationData.filter(location=>{const matchesAddress=!searchAddress||location.address.toLowerCase().includes(searchAddress)||location.name.toLowerCase().includes(searchAddress);const matchesProvince=!selectedProvince||location.province===selectedProvince;const matchesDistrict=!selectedDistrict||location.district===selectedDistrict;return matchesAddress&&matchesProvince&&matchesDistrict});updateLocationsList(filteredLocations);updateMap(filteredLocations)}
function updateLocationsList(locations){const $locationsList=$('#locationsList');$locationsList.empty();$('#locationCount').text(locations.length);if(locations.length===0){$locationsList.html('<p>Không tìm thấy kết quả phù hợp.</p>');return}
locations.forEach(location=>{const locationHtml=`
                    <div class="location-item" data-id="${location.id}">
                        <div class="location-name">
                            <span class="location-icon">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="#e51e25">
                                    <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/>
                                </svg>
                            </span>
                            ${location.name}
                        </div>
                        <div class="location-address">Địa chỉ: ${location.address}</div>
                        <div class="location-hotline">Hotline: ${location.hotline}</div>
                        <div class="location-hours">Giờ mở cửa: ${location.hours}</div>
                        <div class="location-actions">
                            <a class="view-map-btn" data-id="${location.id}">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <circle cx="12" cy="12" r="10"></circle>
                                    <line x1="12" y1="8" x2="12" y2="16"></line>
                                    <line x1="8" y1="12" x2="16" y2="12"></line>
                                </svg>
                                ${title_directions}
                            </a>
                            <a href="${location.googleMapsUrl}" class="google-map-btn" target="_blank">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="15 3 21 3 21 9"></polyline>
                                    <polyline points="9 21 3 21 3 15"></polyline>
                                    <line x1="21" y1="3" x2="14" y2="10"></line>
                                    <line x1="3" y1="21" x2="10" y2="14"></line>
                                </svg>
                                GOOGLE MAPS
                            </a>
                        </div>
                    </div>
                `;$locationsList.append(locationHtml)});$('.location-item').on('click',function(){const locationId=$(this).data('id');selectLocation(locationId)});$('.view-map-btn').on('click',function(e){e.stopPropagation();const locationId=$(this).data('id');selectLocation(locationId)})}
function selectLocation(locationId){$('.location-item').removeClass('active');$(`.location-item[data-id="${locationId}"]`).addClass('active');selectedLocationId=locationId;const location=filteredLocations.find(loc=>loc.id===locationId);if(location){markers.forEach(marker=>{if(marker.getPopup()&&marker.getPopup().isOpen()){marker.getPopup().remove()}});const marker=markers.find(m=>m.getElement().getAttribute('data-id')==locationId);marker.getPopup().addTo(map);map.flyTo({center:[location.coordinates.lng,location.coordinates.lat],zoom:15,essential:!0,complete:function(){if(marker){highlightMarker(locationId);marker.getPopup().addTo(map)}}})}}
function updateMap(locations){markers.forEach(marker=>{if(marker&&marker.remove){marker.remove()}});markers=[];if(locations.length===0)return;locations.forEach(location=>{const marker=createMarker(location);markers.push(marker)});if(locations.length>1){fitMapToBounds(locations)}else if(locations.length===1){map.flyTo({center:[locations[0].coordinates.lng,locations[0].coordinates.lat],zoom:15,essential:!0})}}
function createLocationPopup(location){return new goongjs.Popup({offset:25,closeButton:!0,closeOnClick:!0}).setHTML(`
        <div style="padding: 10px; max-width: 200px;">
            <h3 style="margin: 0 0 5px; color: #e51e25;">${location.name}</h3>
            <p style="margin: 5px 0; font-size: 13px;">${location.address}</p>
            <p style="margin: 5px 0; font-size: 13px;">Hotline: ${location.hotline}</p>
            <p style="margin: 5px 0; font-size: 13px;">Giờ mở cửa: ${location.hours}</p>
            <a href="${location.googleMapsUrl}" target="_blank" style="color: #e51e25; font-size: 13px; display: inline-block; margin-top: 5px; text-decoration: none; outline: none;">Xem trên Google Maps</a>
        </div>
    `)}
function createMarker(location){const existingMarkerIndex=markers.findIndex(m=>m.getElement().getAttribute('data-id')==location.id);if(existingMarkerIndex>-1){markers[existingMarkerIndex].remove();markers.splice(existingMarkerIndex,1)}
const el=document.createElement('div');el.className='map-marker';el.setAttribute('data-id',location.id);const marker=new goongjs.Marker({element:el,anchor:'bottom'}).setLngLat([location.coordinates.lng,location.coordinates.lat]).addTo(map);const popup=createLocationPopup(location);marker.setPopup(popup);el.addEventListener('click',()=>{$('.location-item').removeClass('active');$(`.location-item[data-id="${location.id}"]`).addClass('active');const listContainer=document.querySelector('.list-container');const locationItem=document.querySelector(`.location-item[data-id="${location.id}"]`);if(listContainer&&locationItem){listContainer.scrollTop=locationItem.offsetTop-listContainer.offsetTop}});return marker}
function highlightMarker(locationId){const marker=markers.find(m=>m.getElement().getAttribute('data-id')==locationId);if(marker){const markerEl=marker.getElement();markerEl.classList.add('highlighted');setTimeout(()=>{markerEl.classList.remove('highlighted')},1500)}}
function fitMapToBounds(locations){const bounds=new goongjs.LngLatBounds();locations.forEach(location=>{bounds.extend([location.coordinates.lng,location.coordinates.lat])});if(userLocation){bounds.extend([userLocation.lng,userLocation.lat])}
map.fitBounds(bounds,{padding:50,maxZoom:15,duration:1000})}
function getUserLocation(){if(navigator.geolocation){navigator.geolocation.getCurrentPosition(function(position){userLocation={lat:position.coords.latitude,lng:position.coords.longitude};showUserLocation(userLocation);findNearestLocation(userLocation)},function(error){alert('Không thể xác định vị trí hiện tại. Vui lòng cho phép truy cập vị trí của bạn.');console.error('Error getting user location:',error)})}else{alert('Trình duyệt của bạn không hỗ trợ định vị.')}}
function showUserLocation(location){if(currentLocationMarker){currentLocationMarker.remove()}
const el=document.createElement('div');el.className='map-marker current-location';currentLocationMarker=new goongjs.Marker(el).setLngLat([location.lng,location.lat]).setPopup(new goongjs.Popup({offset:25}).setHTML('<div style="padding: 10px;"><strong>Vị trí của bạn</strong></div>')).addTo(map);fitMapToBounds(filteredLocations)}
function findNearestLocation(userLocation){if(filteredLocations.length===0)return;let nearestLocation=null;let shortestDistance=Infinity;filteredLocations.forEach(location=>{const distance=calculateDistance(userLocation.lat,userLocation.lng,location.coordinates.lat,location.coordinates.lng);if(distance<shortestDistance){shortestDistance=distance;nearestLocation=location}});if(nearestLocation){$('#nearestLocation').addClass('show');$('#nearestLocationContent').html(`
                    <div class="location-name" style="margin-top: 5px;">${nearestLocation.name}</div>
                    <div class="location-address">Địa chỉ: ${nearestLocation.address}</div>
                    <div style="margin-top: 5px;">Khoảng cách: ${formatDistance(shortestDistance)}</div>
                    <div class="location-actions" style="margin-top: 10px;">
                        <a class="view-map-btn" data-id="${nearestLocation.id}">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <circle cx="12" cy="12" r="10"></circle>
                                <line x1="12" y1="8" x2="12" y2="16"></line>
                                <line x1="8" y1="12" x2="16" y2="12"></line>
                            </svg>
                             ${title_directions}
                        </a>
                        <a href="${nearestLocation.googleMapsUrl}" class="google-map-btn" target="_blank">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="15 3 21 3 21 9"></polyline>
                                <polyline points="9 21 3 21 3 15"></polyline>
                                <line x1="21" y1="3" x2="14" y2="10"></line>
                                <line x1="3" y1="21" x2="10" y2="14"></line>
                            </svg>
                            GOOGLE MAPS
                        </a>
                    </div>
                `);$('#nearestLocationContent .view-map-btn').on('click',function(){const locationId=$(this).data('id');selectLocation(locationId)});selectLocation(nearestLocation.id)}}
function calculateDistance(lat1,lon1,lat2,lon2){const R=6371;const dLat=deg2rad(lat2-lat1);const dLon=deg2rad(lon2-lon1);const a=Math.sin(dLat/2)*Math.sin(dLat/2)+Math.cos(deg2rad(lat1))*Math.cos(deg2rad(lat2))*Math.sin(dLon/2)*Math.sin(dLon/2);const c=2*Math.atan2(Math.sqrt(a),Math.sqrt(1-a));const d=R*c;return d}
function deg2rad(deg){return deg*(Math.PI/180)}
function formatDistance(distance){if(distance<1){return `${Math.round(distance * 1000)} m`}else{return `${distance.toFixed(1)} km`}}
let selectedLocationId=null;$('#zoomIn').on('click',function(){const currentZoom=map.getZoom();zoomMap(currentZoom+1)});$('#zoomOut').on('click',function(){const currentZoom=map.getZoom();zoomMap(currentZoom-1)});function zoomMap(newZoom){if(selectedLocationId){const location=filteredLocations.find(loc=>loc.id===selectedLocationId);if(location){map.flyTo({center:[location.coordinates.lng,location.coordinates.lat],zoom:newZoom,essential:!0});return}}
map.zoomTo(newZoom,{duration:500})}})})(jQuery)
;