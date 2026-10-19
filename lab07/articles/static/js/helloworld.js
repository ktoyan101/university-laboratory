console.log("students script ready");

var classmates = [
    { name: "Мария", surname: "Орлова", group: "БВТ2201", marks: [5, 4, 5] },
    { name: "Павел", surname: "Новиков", group: "БСТ2203", marks: [4, 3, 4] },
    { name: "Елена", surname: "Васильева", group: "БВТ2201", marks: [5, 5, 4] },
    { name: "Роман", surname: "Фёдоров", group: "БАП2102", marks: [3, 4, 3] },
    { name: "Ольга", surname: "Морозова", group: "БСТ2203", marks: [5, 4, 5] }
];

console.log(classmates);

function padRight(value, size) {
    var text = String(value);
    while (text.length < size) {
        text += " ";
    }
    return text;
}

function showStudentsTable(list) {
    console.log(
        padRight("Имя", 15),
        padRight("Фамилия", 15),
        padRight("Группа", 10),
        padRight("Оценки", 20)
    );
    for (var i = 0; i < list.length; i++) {
        console.log(
            padRight(list[i].name, 15),
            padRight(list[i].surname, 15),
            padRight(list[i].group, 10),
            padRight(list[i].marks, 20)
        );
    }
    console.log("");
}

showStudentsTable(classmates);

function filterStudentsByGroup(list) {
    var groupName = prompt("Группа для фильтрации:");
    if (groupName === null) {
        return;
    }
    var found = [];
    for (var i = 0; i < list.length; i++) {
        if (list[i].group === groupName) {
            found.push(list[i]);
        }
    }
    console.log("Результат по группе", groupName);
    if (found.length === 0) {
        console.log("Никого не найдено");
    } else {
        showStudentsTable(found);
    }
}

filterStudentsByGroup(classmates);

function filterStudentsByMark(list) {
    var minAvg = parseFloat(prompt("Минимальный средний балл:"));
    if (isNaN(minAvg)) {
        console.log("Нужно число");
        return;
    }
    var found = [];
    for (var i = 0; i < list.length; i++) {
        var sum = 0;
        for (var j = 0; j < list[i].marks.length; j++) {
            sum += list[i].marks[j];
        }
        if (sum / list[i].marks.length > minAvg) {
            found.push(list[i]);
        }
    }
    console.log("Средний балл >", minAvg);
    if (found.length === 0) {
        console.log("Никого не найдено");
    } else {
        showStudentsTable(found);
    }
}

filterStudentsByMark(classmates);
