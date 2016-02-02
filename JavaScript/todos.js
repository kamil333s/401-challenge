// Kevin Smith
// 1-22-16
// Code Fellows 401-Python Coding Challenge
// Todo Manager

// Description: Make a simple html page to manage Todos.
// It should have an input field. When the user enters text in the
// input field, add that input to the top of the Todo list. When
// an existing item is clicked, it should disappear from the page.
// In addition to pushing the answer to your Github account,
// please also setup a http://jsfiddle.net/ with the solution
// and paste in the saved URL here.

// Comments: My solution manages the to-do list on the HTML page.
// The list therefore is not persistent and will be gone when the page
// is closed. The code is not the most efficient or consistent.
// For example, I tried to illustrate different methods of click event handling.

"use strict";
var toDoList = document.getElementById('toDoList');
var taskButton = document.getElementById('btn_task');
var taskField = document.getElementById('input');

function setFocus() {
    taskField.focus();
}

function addNewTask() {
    // Get current to do list and identify the first item
    var firstElement = toDoList.getElementsByTagName("li")[0];

    // Get new entry from form field
    var newTemp = document.getElementById('input');
    var newTask = newTemp.value;

    // Create new list item
    var newElement = document.createElement('li');

    // Create text for new task list item
    // ***Could use innerHTML, but chose to be explicit***
    // newElement.innerHTML = newTask
    var taskText = document.createTextNode(newTask);
    newElement.appendChild(taskText);

    // Put new task first in the list
    toDoList.insertBefore(newElement, firstElement);
}

function submitTask() {
    if (taskField.value !== '' && taskField !== 'New task to do') {
        addNewTask();
        taskField.value = '';
    }
}


// I chose to use different types of click event handlers just to illustrate their use.


// New task button click event handler
taskButton.onclick = function () {
    if (taskField.value !== '' && taskField.value !== "New task to do") {
        submitTask();
    }
    setFocus();
};

// List item click event handler
document.getElementById('toDoList').addEventListener('click', function (e) {
    if (e.target && e.target.nodeName === 'LI') {
        toDoList.removeChild(e.target);
    }
});

// When enter is pressed, add the task
document.getElementById('taskForm').onsubmit = function () {
    submitTask();
    // Prevents form from submitting and reloading page
    return false;
};

// Toggle default placeholder text in the form field
taskField.onfocus = function () {
    if (taskField.value === "New task to do") {
        taskField.value = "";
    }
};

// Toggle default placeholder text in the form field
taskField.onblur = function () {
    if (taskField.value === "") {
        taskField.value = "New task to do";
    }
};