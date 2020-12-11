function rewindDate(direction){
    let params = GETParamsAsObject()
    let date = new Date()

    if ('date' in params){
        const [year, month, day] = params.date.split('-').map((x)=>parseInt(x,10))
        date = new Date(year, month-1, day)
    }

    if (direction === 'next'){
        date = new Date(date.getTime() + 1000*60*60*24)
    } else if (direction === 'prev'){
        date = new Date(date.getTime() - 1000*60*60*24)
    }

    params.date = formatDate(date)
    const search = Object.keys(params).reduce((acc, val) => `${acc}${val}=${params[val]}&`, '?')
    window.location.search = search.slice(0, -1)
}

function formatDate (date){
    let day = date.getDate() < 10 ? // дни возвращает от 1
        "0" + date.getDate().toString()
        : date.getDate().toString();
    let month = date.getMonth() + 1 < 10 ? // месяцы возвращает от 0
        "0" + (date.getMonth() + 1).toString()
        : (date.getMonth() + 1).toString();
    let year = date.getFullYear().toString();

    return [year, month, day].join('-')
}
function GETParamsAsObject() {
    let searchString = window.location.search.slice(1) //вытаскиваем get параметры, slice(1) обрезаем '?'
    if (searchString === '') {
        return {}
    }
    return Object.fromEntries(searchString.split('&').map(item => item.split('='))) // получаем массив строк, который состоит из списка {переменная, значение}
    // Object.fromEntries собирает этот список списков в словарь
}