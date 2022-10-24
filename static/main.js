function showToast(text) {
  var x = document.getElementById("toast");
  x.innerHTML = text;
  x.className = "show";
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 1900);
}

function setLikeButtonBackground(color) {
    document.getElementById("like-btn").style.background = color;

}

function refreshLikeCounter(counter) {
    document.getElementById("like-counter").innerHTML = counter;
}

function removePublishButton(btnId) {
    document.getElementById(btnId).remove();
}

function removeTableRowById(id) {
    document.getElementById('task-table-row-' + id).remove();
}

function updateTaskStatus(id, status) {
    var element = document.getElementById('table-status-' + id);
    element.innerHTML = status;
}

function updateLastUpdateDate(id, updateDate) {
    var element = document.getElementById('table-update-date-' + id);
    element.innerHTML = updateDate;
}

function removeChangeStatusButton(id) {
    document.getElementById('table-status-btn-' + id).remove();
}

function sortTable(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("task-table");
  switching = true;
  dir = "asc";
  while (switching) {
    switching = false;
    rows = table.rows;
    for (i = 1; i < (rows.length - 1); i++) {
      shouldSwitch = false;
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          shouldSwitch = true;
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      switchcount ++;
    } else {
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}
