#zone is the variable that will contains the zone that will be used in the API calls
zone=None

#list the existing zones 
zones=compute_service.zones().list(project=projectId).execute()
#list that will contains the zones for a dropdown list
zonesList=[item['name'] for item in zones['items']]
zonesList.append('none')

#the dropdownlist widget
zoneWidget=widgets.Dropdown(options=zonesList,value='none',description='Choose your Zone:')
zoneValid=widgets.Valid(value=False,description='')
display(widgets.Box([zoneWidget,zoneValid]))

def zoneValueChange(sender):
    if zoneWidget.value!='none':
        #when a vail zone is slected, the variable zone is set
        zoneValid.value=True
        zoneValid.description=zoneWidget.value
        global zone
        zone=zoneWidget.value   
    else:
        zoneValid.value=False
        zoneValid.description=''
        
zoneWidget.observe(zoneValueChange, 'value')    