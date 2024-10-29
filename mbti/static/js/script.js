// Variável para rastrear a pergunta atual
let currentQuestion = 1;
const totalQuestions = 16;

function nextQuestion() {
    // Se já está na última pergunta e o botão foi clicado para finalizar, exibe o alerta e finaliza
    if (currentQuestion > totalQuestions) {
        alert("Teste finalizado! Verifique seus resultados.");
        // Aqui você pode redirecionar para a página de resultados, se desejado
        // window.location.href = "/resultados.html";
        return;
    }

    // Esconde a pergunta atual
    document.getElementById(`question-${currentQuestion}`).style.display = "none";

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
    // Esconde todas as perguntas, exceto a primeira
    for (let i = 1; i <= totalQuestions; i++) {
        if (i === 1) {
            document.getElementById(`question-${i}`).style.display = "block";
        } else {
            document.getElementById(`question-${i}`).style.display = "none";
        }
    }
}

// Executa a função de inicialização ao carregar a página
window.onload = initializeQuestions;
