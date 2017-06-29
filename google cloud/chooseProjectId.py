#projectId is the variable that will contains the projectId that will be used in the API calls
projectId=None

#list the existing projects 
projects=resource_service.projects().list().execute()
#we create a dictionaray name:projectId for a dropdown list widget
projectsList={project['name']:project['projectId'] for project in projects['projects']}
projectsList['None']='invalid'

#the dropdownlist widget
projectWidget=widgets.Dropdown(options=projectsList,description='Choose your Project',value='invalid')
#a valid widget that get valid when a project is selected
projectIdValid=widgets.Valid(value=False,description='')
display(widgets.Box([projectWidget,projectIdValid]))

def projectValueChange(sender):
    if projectWidget.value!='invalid':
        #when a valid project is selected ,the gloabl variable projectId is set 
        projectIdValid.value=True
        projectIdValid.description=projectWidget.value
        global projectId
        projectId=projectWidget.value    
    else:
        projectIdValid.value=False
        projectIdValid.description=''
projectWidget.observe(projectValueChange, 'value')