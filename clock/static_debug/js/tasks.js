
/* #### Persistent Variables ############################################### */
var color_str = '888888';
var p_color_str = '444444';

/* #### Clock in ########################################################### */
function clock_in(task_id) {
  document.getElementById("id_task_id").value = task_id;
  document.getElementById("task_id_form").submit();
}

/* #### Add Task ########################################################### */
function show_add_task(project) {
  color_str='888888';
  if (project != 0) {
    var p_name = document.getElementById("p_label"+project).innerHTML;
    document.getElementById("new_task_label").innerHTML="New " + p_name + " Task:";
  } else {
    document.getElementById("new_task_label").innerHTML="New Task:";
  }
  document.getElementById("task_modal").style.display="block";
  document.getElementById("add_buttons_section").style.display="none";
  document.getElementById("id_project_id").value=project;
}

function hide_add_task() {
  document.getElementById("id_name").value="";
  document.getElementById("task_modal").style.display="none";
  document.getElementById("add_buttons_section").style.display="block";
  task_color(0);
}

function submit_add_task() {
  document.getElementById("id_color").value=color_str;
  document.getElementById("task_form").submit();
}

function task_color(t) {
  colors = ['888888', '999999', 'AAAAAA', 'BBBBBB', 'CCCCCC', 'DDDDDD'];
  color_str = colors[t];
  for(j=0;j<6;j++) {
    t==j?document.getElementById("tb"+j).setAttribute("disabled","disabled")
    :document.getElementById("tb"+j).removeAttribute("disabled");
  }
}

/* #### Edit Task ########################################################## */
function edit_task(task_id) {

}

function delete_task(task_id) {

}

/* #### Add Project ######################################################## */
function show_add_project() {
  p_color_str='444444';
  document.getElementById("project_modal").style.display="block";
  document.getElementById("add_buttons_section").style.display="none";
}

function hide_add_project() {
  document.getElementById("id_p_name").value="";
  document.getElementById("project_modal").style.display="none";
  document.getElementById("add_buttons_section").style.display="block";
  project_color(0);
}

function submit_add_project() {
  document.getElementById("id_p_color").value=p_color_str;
  document.getElementById("project_form").submit();
}

function project_color(t) {
  colors = ['444444', '555555', '666666'];
  p_color_str = colors[t];
  for(j=0;j<6;j++) {
    t==j?document.getElementById("pb"+j).setAttribute("disabled","disabled")
    :document.getElementById("pb"+j).removeAttribute("disabled");
  }
}

/* #### Edit Project ####################################################### */
function edit_project() {

}

function delete_project() {
  
}

/* #### Show/Hide Project tasks ############################################ */
function show_project_tasks(project_id) {
  var p_tasks = document.getElementById("p_tasks"+project_id);
  if (p_tasks.style.display == "none") {
    p_tasks.style.display="block";
    document.getElementById("drop"+project_id).className="glyphicon glyphicon-triangle-bottom";
  } else {
    p_tasks.style.display="none";
    document.getElementById("drop"+project_id).className="glyphicon glyphicon-triangle-right";
  }
}


