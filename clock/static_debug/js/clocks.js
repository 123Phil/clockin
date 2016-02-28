
/* #### Persistent Variables ############################################### */
var clocked_in = false;
var click_clocking = false;
var start_time = 0;
var elapsed_time = 0;
var time_by_id = document.getElementById("time0");
var current_task = 0;
var color_str = '000000';


/* #### ajax POST ########################################################## */
function ajax_post(url, post_data) {
  var retval = false;
  $.ajax({
    url: url,
    method: "POST",
    data: post_data,
    dataType: "html"
  }).done(function() {
    retval = true;
  }).fail(function(msg) {
    alert(msg)
  });
  return retval;
}

/* #### Format helper functions ############################################ */
function pad(num) {
  var s = "00" + num;
  return s.substr(s.length - 2);
}

function enbold(str) {
  return "<b>" + str + "</b>"
}

function time_string(h, m, s) {
  time_str = enbold(pad(h)) + " H ";
  time_str += enbold(pad(m)) + " M ";
  time_str += enbold(pad(s)) + " S";
  return time_str;
}

/* #### Clock in/out ####################################################### */
function click_clock(task_id) {
  if (!click_clocking) {
    
    //TODO: disable the button...

    click_clocking = true;
    if (!clocked_in) {
      time_by_id = document.getElementById("time" + task_id);
      clock_in(task_id);
    } else {
      if (current_task != task_id) {
        return;
      }
      clock_out(task_id);
    }
    click_clocking = false;
  }
}

function clock_in(task_id) {
  clocked_in = true;
  current_task = task_id;
  start_time = (new Date()).getTime();
  timer_interval = setInterval("update_timer()", 1000);
  $('#clock_butt' + task_id).toggleClass('btn-success');
  $('#clock_butt' + task_id).toggleClass('btn-warning');
}

function clock_out(task_id) {
  clearInterval(timer_interval);
  var s = Math.floor(elapsed_time / 1000);
  var csrf = $('[name="csrfmiddlewaretoken"]').value;
  if (ajax_post("clocks/clockout", {id : task_id, seconds : s, csrfmiddlewaretoken : csrf})) {
    time_by_id.innerHTML = time_string(0,0,0);
    clocked_in = false;
    current_task = 0;
    $('#clock_butt' + task_id).toggleClass('btn-success');
    $('#clock_butt' + task_id).toggleClass('btn-warning');
    $('#clock_butt' + task_id).removeClass('btn-danger');
  } else {
    $('#clock_butt' + task_id).removeClass('btn-success');
    $('#clock_butt' + task_id).removeClass('btn-warning');
    $('#clock_butt' + task_id).addClass('btn-danger');
  }    
}

function update_timer() {
  elapsed_time = ((new Date()).getTime() - start_time);
  var h = m = s = 0;

  s = Math.floor(elapsed_time / 1000);
  m = Math.floor(s / 60) % 60;
  h = Math.floor(m / 60);
  s = s % 60;

  time_by_id.innerHTML = time_string(h, m, s);
}

/* #### Add Task ########################################################### */
function show_add_task(project) {
  document.getElementById("task_modal").style.display="block";
  document.getElementById("add_buttons_section").style.display="none";
  document.getElementById("id_project").value=project;
}

function hide_add_task() {
  document.getElementById("id_name").value="";
  task_color(0);
  document.getElementById("task_modal").style.display="none";
  document.getElementById("add_buttons_section").style.display="block";
}

function submit_add_task() {
  document.getElementById("id_color").value=color_str;
  document.getElementById("task_form").submit();
}

function task_color(t) {
  colors = ['333333', '555555', '777777', '999999', 'BBBBBB'];
  color_str = colors[t];
  for(j=0;j<5;j++) {
    t==j?document.getElementById("tb"+j).setAttribute("disabled","disabled")
    :document.getElementById("tb"+j).removeAttribute("disabled");
  }
}

/* #### Edit Task ########################################################## */
function edit_task() {

}

function delete_task() {

}

/* #### Add Project ######################################################## */
function show_add_project() {

}

function hide_add_project() {

}

function submit_add_project() {

}

/* #### Edit Project ####################################################### */
function edit_project() {

}

function delete_project() {
  
}






