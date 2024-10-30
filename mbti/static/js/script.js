// Variável para rastrear a pergunta atual
let currentQuestion = 1;
const totalQuestions = 16;
let form_data = {}
let data = JSON.parse(document.getElementById('received_data').textContent);


function nextQuestion() {
    // Se já está na última pergunta e o botão foi clicado para finalizar, exibe o alerta e finaliza
    console.log(data)
    console.log("Passed")
    if (currentQuestion > totalQuestions) {
        alert("Teste finalizado! Verifique seus resultados.");
        // Aqui você pode redirecionar para a página de resultados, se desejado
        // window.location.href = "/resultados.html";
        return;
    }
    
    document.getElementById(`question-${currentQuestion}`).innerHTML.textContent = "";
    
    // Incrementa o número da pergunta
    currentQuestion++;
    
    // Exibe a próxima pergunta, se ainda houver
    if (currentQuestion <= totalQuestions) {
        document.getElementById(`question-${currentQuestion}`).style.display = "block";
    }
    
    // Se estamos na última pergunta, altera o botão para "Finalizar teste"
    if (currentQuestion === totalQuestions) {
        document.getElementById("nextButton").innerText = "Finalizar teste";
    }
}

// Função para inicializar a visibilidade das perguntas ao carregar a página
function initializeQuestions() {
    console.log(data.questions[0].question, typeof(data.questions[0].question))
    document.getElementById("question-title").innerHTML = data.questions[0].question
    document.getElementById("answer-text-left").innerHTML = data.questions[0].responses.E[0]
    document.getElementById("answer-text-right").innerHTML = data.questions[0].responses.I[0]
}

// Executa a função de inicialização ao carregar a tag (O json deve ser carregado antes desse script);
initializeQuestions()
