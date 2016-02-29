
/* #### Persistent Variables ############################################### */
var start_time = 0;
var elapsed_time = 0;
var total_time = 0;
var initial_total = 0;
var timer_interval = null;

/* #### Format helper functions ############################################ */
function pad(num) {
  var s = "00" + num;
  return s.substr(s.length - 2);
}

function enbold(str) {
  return "<b>" + str + "</b>"
}

function time_string(h, m, s) {
  var time_str = "";
  if (h > 0) {
    time_str = enbold(h) + " H ";
  }
  time_str += enbold(pad(m)) + " M ";
  time_str += enbold(pad(s)) + " S";
  return time_str;
}

/* #### Clock ############################################################## */
function clock_out(task_id) {
  clearInterval(timer_interval);
  elapsed_time = ((new Date()).getTime() - start_time);
  var s = Math.floor(elapsed_time / 1000);
  document.getElementById("id_elapsed").value = s;
  document.getElementById("clock_form").submit();
}

function update_timer() {
  // Current clock-in
  elapsed_time = ((new Date()).getTime() - start_time);
  var h = m = s = 0;
  s = Math.floor(elapsed_time / 1000);
  m = Math.floor(s / 60) % 60;
  h = Math.floor(s / 3600);
  s = s % 60;
  document.getElementById("task_clock").innerHTML = time_string(h, m, s) + " on the clock";
  // Total time
  total_time = initial_total + elapsed_time;
  s = Math.floor(total_time / 1000);
  m = Math.floor(s / 60) % 60;
  h = Math.floor(s / 3600);
  s = s % 60;
  document.getElementById("task_total").innerHTML = time_string(h,m,s) + " task total";
}

function init_times(start, total) {
  start_time = (new Date()).getTime() - (start*1000);
  total_time = initial_total = total*1000;
}




