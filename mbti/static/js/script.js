// Variável para rastrear a pergunta atual
let currentQuestion = 0;
let currentAnswer = 0;
const totalQuestions = 16;
let form_data = {}
let data = JSON.parse(document.getElementById('received_data').textContent);


function nextQuestion() {
    // Se já está na última pergunta e o botão foi clicado para finalizar, exibe o alerta e finaliza
    currentAnswer++
    let a1 = Object.values(data.questions[currentQuestion].responses)[0]
    let a2 = Object.values(data.questions[currentQuestion].responses)[1]
    if (a1[currentAnswer] == undefined) {
        currentQuestion++
        currentAnswer = 0
        initializeQuestions()
    }
    console.log(a1)
    document.getElementById("answer-text-left").innerHTML = a1[currentAnswer]
    document.getElementById("answer-text-right").innerHTML = a2[currentAnswer]
}

// Função para inicializar a visibilidade das perguntas ao carregar a página
function initializeQuestions() {
    console.log(data)
    document.getElementById("question-number").innerHTML = "Questão "+(currentQuestion + 1)
    document.getElementById("question-title").innerHTML = data.questions[currentQuestion].question
    let a1 = Object.values(data.questions[currentQuestion].responses)[0]
    let a2 = Object.values(data.questions[currentQuestion].responses)[1]
    document.getElementById("answer-text-left").innerHTML = a1[0]
    document.getElementById("answer-text-right").innerHTML = a2[0]
}

// Executa a função de inicialização ao carregar a tag (O json deve ser carregado antes desse script);
initializeQuestions()
