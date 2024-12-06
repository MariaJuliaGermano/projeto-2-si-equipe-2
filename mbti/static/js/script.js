// Variável para rastrear a pergunta atual
let currentQuestion = 0;
let currentAnswer = 0;
const totalQuestions = 16;
let form_data = []
let data = JSON.parse(document.getElementById('received_data').textContent);
let count = 0;

function lastQuestion() {
    form_data.pop()
    count--
    document.getElementById("counter-bar").style.width = (count/48)*100+"%"
    document.getElementById("counter").innerHTML = count+"/48"
    currentAnswer--
    document.getElementById("answer-text-left").innerHTML = a1[currentAnswer]
    document.getElementById("answer-text-right").innerHTML = a2[currentAnswer]
    console.log(form_data)
}

function nextQuestion() {
    if (document.getElementById("answer-left").checked) {
        form_data.push(Object.keys(data.questions[currentQuestion].responses)[0])
    } else if (document.getElementById("answer-right").checked) {
        form_data.push(Object.keys(data.questions[currentQuestion].responses)[1])
    } else{
        alert("selecione uma das alternativas para avançar para a próxima pergunta")
        return 0
    }
    count++
    document.getElementById("counter-bar").style.width = (count/48)*100+"%"
    document.getElementById("counter").innerHTML = count+"/48"

    currentAnswer++
    let a1 = Object.values(data.questions[currentQuestion].responses)[0]
    let a2 = Object.values(data.questions[currentQuestion].responses)[1]
    if (a1[currentAnswer] == undefined) {
        currentQuestion++
        if (data.questions[currentQuestion] == undefined) {
            console.log("end of test")
            console.log(data)
            console.log(form_data)
            document.getElementById("form-data").value = form_data
            document.getElementById("answer-section").hidden = true
            document.getElementById("submit-section").hidden = false
        } else {
            currentAnswer = 0
            initializeQuestions()
        }
    } else {
        document.getElementById("answer-text-left").innerHTML = a1[currentAnswer]
        document.getElementById("answer-text-right").innerHTML = a2[currentAnswer]
    }
    console.log(form_data)
}

// Função para inicializar a visibilidade das perguntas ao carregar a página
function initializeQuestions() {
    document.getElementById("question-title").innerHTML = data.questions[currentQuestion].question
    let a1 = Object.values(data.questions[currentQuestion].responses)[0]
    let a2 = Object.values(data.questions[currentQuestion].responses)[1]
    document.getElementById("answer-text-left").innerHTML = a1[0]
    document.getElementById("answer-text-right").innerHTML = a2[0]
}
document.getElementById("submit-section").hidden = true
// Executa a função de inicialização ao carregar a tag (O json deve ser carregado antes desse script);
initializeQuestions()
