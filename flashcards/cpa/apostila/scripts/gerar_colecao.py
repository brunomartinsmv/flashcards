from pathlib import Path
import csv, json, re
ROOT=Path('flashcards/cpa/apostila')
DECK_ROOT=ROOT.parent
plan=json.loads(Path('flashcards/cpa/fontes/plano_estudos.json').read_text(encoding='utf-8'))
deck_names={}
for item in plan:
 n=int(re.search(r'CPA\s+(\d+)',item['titulo']).group(1))
 title=re.split(r'\s+—\s+',item['titulo'],maxsplit=1)[1].replace('/',' e ')
 deck_names[n]=f'CPA::{n:02d} {title}'
# tuple: module, question, answer, printed page, theme tags
C=[]
def add(n, qs):
 for q,a,p,t in qs: C.append((n,q,a,p,t))
add(3,[
('Como diferenciar risco de crédito de risco de mercado?','Crédito é a possibilidade de a contraparte não pagar como prometido. Mercado é a oscilação do valor do ativo por mudanças em preços, juros, câmbio ou outros fatores de mercado.','41','riscos credito mercado'),
('O que distingue risco de liquidação de risco de crédito?','No risco de liquidação, uma parte entrega recursos ou ativos e a contraparte pode não cumprir a etapa correspondente no momento devido. A exposição decorre do intervalo e do processo de liquidação.','41','riscos liquidacao'),
('Como a diversificação reduz risco de carteira?','A combinação de ativos com fontes de risco diferentes, especialmente com baixa correlação, reduz a dependência de um único fator. Ter muitos ativos parecidos não garante diversificação.','45','riscos diversificacao'),
('O que é risco de reinvestimento?','É o risco de os fluxos recebidos, como cupons, precisarem ser aplicados novamente a taxas menores que as originalmente esperadas.','49','riscos reinvestimento'),
('Que papel a BSM exerce no mercado?','A BSM supervisiona os mercados administrados pela B3, monitora operações e condutas e atua para preservar integridade e confiança no mercado.','51','autorregulacao bsm'),
('Quais frentes gerais caracterizam a autorregulação de mercado?','Entidades autorreguladoras estabelecem padrões para participantes, monitoram o cumprimento e podem apurar condutas e aplicar medidas dentro de seu âmbito. Sua atuação complementa a supervisão estatal.','53','autorregulacao'),
('O que a Anbima faz na distribuição de investimentos?','A Anbima estabelece regras de autorregulação para instituições aderentes, promove padrões de conduta e transparência e acompanha seu cumprimento.','54','autorregulacao anbima'),
('Que cuidado o Código de Distribuição exige antes de recomendar um produto?','A recomendação deve considerar objetivos, situação financeira, conhecimento e tolerância a risco do cliente, além das características, riscos, custos, liquidez e garantias do produto.','58','distribuicao suitability'),
('Quando a instituição deve atualizar o perfil do investidor?','Quando houver mudança relevante nas informações do cliente e nos prazos definidos pelas regras aplicáveis. A instituição deve manter o perfil atualizado antes de apoiar recomendações nele.','62','distribuicao suitability'),
('Por que uma garantia não torna um investimento sem risco?','A garantia cobre apenas situações e limites definidos. Permanecem riscos como oscilação de preço, liquidez, prazo e perdas que excedam a cobertura.','179','garantias riscos'),
])
add(4,[
('Como funciona a entrada de dados na HP-12C com notação polonesa reversa?','Digite o primeiro número e pressione ENTER; depois digite o segundo e escolha a operação. Exemplo: 5 ENTER 3 × calcula 15.','65','hp12c calculadora'),
('Qual é a diferença entre taxa nominal e taxa real?','A taxa nominal é observada sem descontar a inflação. A taxa real mede o ganho de poder de compra: (1 + taxa nominal) / (1 + inflação) − 1.','69','taxas inflacao'),
('Quanto rende em termos reais uma aplicação de 15% com inflação de 9%?','(1,15 / 1,09) − 1 = 0,0550, aproximadamente 5,50% no período. Não se obtém a taxa real exata apenas subtraindo as taxas.','69','taxas calculo'),
('Qual é a fórmula do montante em juros compostos?','M = C(1+i)^n, com capital C, taxa por período i e número de períodos n. Taxa e período precisam estar na mesma unidade.','70','juros compostos formula'),
('Qual é o valor futuro de R$ 1.000 a 2% ao mês por 3 meses, com capitalização composta?','M = 1.000 × (1,02)^3 = R$ 1.061,21, aproximadamente.','70','juros compostos calculo'),
('Como converter uma taxa mensal efetiva em taxa anual efetiva?','Use equivalência composta: i_a = (1+i_m)^12 − 1. Para 1% ao mês, (1,01)^12 − 1 ≈ 12,68% ao ano.','73','taxas equivalentes'),
('Como calcular a taxa real de um investimento com retorno de 15% e inflação de 5%?','(1,15 / 1,05) − 1 = 9,52% aproximadamente. A relação multiplicativa mantém o poder de compra corretamente.','72','taxas calculo'),
('Como combinar retornos de dois períodos consecutivos?','Multiplique os fatores de crescimento e subtraia 1: retorno acumulado = (1+r1)(1+r2)−1. Exemplo: 10% e depois −10% resulta em −1%, não zero.','77','rentabilidade acumulada'),
])
add(5,[
('Como funciona o sistema Price?','A prestação tende a ser constante, sob taxa e periodicidade constantes. No início, os juros ocupam parcela maior e a amortização é menor; com a queda do saldo, a amortização cresce.','84','price amortizacao'),
('Como se calcula cada prestação no sistema Price?','A prestação uniforme é PMT = PV × i / [1−(1+i)^−n], em que PV é o principal financiado, i a taxa por período e n o número de parcelas.','85','price formula'),
('Como funciona o SAC?','A amortização do principal é constante: A = PV/n. Como os juros incidem sobre saldo devedor decrescente, as prestações começam maiores e diminuem ao longo do tempo.','88','sac amortizacao'),
('Qual é a prestação inicial de um SAC de R$ 12.000 em 12 meses a 1% ao mês?','Amortização mensal = 12.000/12 = R$ 1.000. Juros iniciais = 1% × 12.000 = R$ 120. Primeira prestação = R$ 1.120.','89','sac calculo'),
('Como comparar Price e SAC para o mesmo principal, prazo e taxa?','Price mantém prestações niveladas; SAC amortiza o principal em parcelas iguais e reduz a prestação com o tempo. O SAC exige pagamentos iniciais maiores e, em condições iguais, tende a gerar menos juros totais.','84,88','price sac comparacao'),
])
add(6,[
('O que representa o WACC?','É o custo médio ponderado das fontes de financiamento da empresa, combinando capital próprio e de terceiros segundo seus pesos. Serve como referência de custo de capital.','95','wacc'),
('Como calcular o custo médio ponderado de capital?','WACC = (PL/V)×Ke + (D/V)×Kd×(1−T), quando o custo da dívida é ajustado pelo benefício fiscal; V = PL + D. Use pesos e premissas consistentes com o problema.','95','wacc formula'),
('O que mede a duration de Macaulay?','O prazo médio ponderado dos fluxos de caixa de um título, usando como pesos os valores presentes de cada fluxo. Um título com cupons pode ter duration menor que seu vencimento.','96','duration'),
('Como interpretar a relação entre juros de mercado e preço de um título prefixado?','Em geral, se a taxa de mercado sobe, o preço presente dos fluxos cai; se a taxa cai, o preço sobe. A duration ajuda a estimar a sensibilidade do preço.','99','duration juros'),
('O que é desconto bancário simples?','É a antecipação de um valor futuro mediante desconto calculado antes do vencimento. No desconto comercial simples, D = N×d×t e o valor liberado é N−D, com taxa e prazo na mesma base.','102','desconto formula'),
('Como usar o VPL para decidir sobre um investimento?','Desconte os fluxos futuros pela taxa mínima requerida e some o investimento inicial: VPL = Σ FC_t/(1+k)^t. VPL positivo indica criação de valor sob as premissas adotadas.','112','investimentos vpl'),
('O que significa a TIR de um projeto?','É a taxa que zera o VPL dos fluxos de caixa. A decisão exige comparação com a taxa mínima atrativa e cautela quando há fluxos não convencionais ou projetos mutuamente excludentes.','104','investimentos tir'),
('O que o payback descontado acrescenta ao payback simples?','Desconta os fluxos pela taxa requerida antes de acumular os valores até recuperar o investimento inicial. Considera valor do dinheiro no tempo, embora ignore fluxos posteriores à recuperação.','115','payback'),
])
add(7,[
('O que o PIB mede pela ótica da produção?','O valor dos bens e serviços finais produzidos dentro do território econômico em determinado período, evitando dupla contagem de insumos intermediários.','124','pib'),
('Qual é a diferença entre inflação de demanda e de custos?','A inflação de demanda decorre de procura agregada acima da capacidade de oferta. A inflação de custos surge quando aumentos de custos de produção pressionam preços.','125','inflacao'),
('Como distinguir Selic Meta de Selic Over?','Selic Meta é a taxa definida como objetivo de política pelo Copom. Selic Over é a taxa efetiva média das operações compromissadas de um dia lastreadas em títulos públicos.','127','selic copom'),
('Como uma alta da Selic tende a afetar consumo e inflação?','Crédito e custo de oportunidade tendem a subir, o que pode conter consumo e demanda; com defasagem, isso ajuda a reduzir pressão inflacionária. O efeito não é imediato nem mecânico.','133','politica monetaria'),
('Quais instrumentos clássicos o Banco Central usa para administrar liquidez?','Operações de mercado aberto, recolhimentos compulsórios e redesconto são instrumentos descritos na apostila para influenciar liquidez e condições monetárias.','136','politica monetaria'),
('O que diferencia política fiscal de política monetária?','Política fiscal atua por receitas e despesas públicas. Política monetária atua sobre juros, moeda e liquidez, sob condução do Banco Central.','135','politicas economicas'),
('Como uma depreciação cambial afeta importações e exportações?','A moeda estrangeira fica mais cara em moeda local: importações tendem a encarecer e exportadores podem receber mais moeda local por receitas externas, dependendo de custos e contratos.','147','cambio'),
])
add(9,[
('Quais são as três formas usuais de remuneração da renda fixa?','Prefixada, pós-fixada e híbrida. A prefixada define taxa nominal; a pós-fixada acompanha um indexador; a híbrida combina indexador e componente prefixado.','154','renda_fixa remuneracao'),
('O que é preço unitário (PU) de um título?','É o preço de negociação do título em uma data. O PU reflete o valor presente dos fluxos futuros segundo as condições de mercado.','155','renda_fixa pu'),
('O que acontece com o preço de um título prefixado quando a taxa de mercado sobe?','O preço tende a cair, pois os fluxos fixos passam a ser descontados por uma taxa maior. Se mantido até o vencimento, o fluxo contratado permanece, ressalvados riscos do emissor e condições do título.','157','tesouro precificacao'),
('Como se caracteriza o Tesouro Selic?','É título público pós-fixado ligado à taxa Selic. Em geral apresenta menor oscilação de preço que títulos prefixados ou indexados à inflação, mas pode haver variação e custos de resgate.','159','tesouro selic'),
('Como se caracteriza um título público indexado ao IPCA?','Combina atualização pela inflação medida pelo IPCA e taxa real prefixada, podendo pagar cupons ou concentrar o pagamento no vencimento, conforme o título.','161','tesouro ipca'),
])
add(10,[
('O que é um CDB?','Título de dívida emitido por banco para captar recursos. A remuneração e o vencimento seguem as condições da emissão; o investidor assume risco de crédito do emissor.','167','titulos_bancarios cdb'),
('Como diferenciar CDB, LCI e LCA pela finalidade?','CDB capta recursos de forma geral. LCI se relaciona ao financiamento imobiliário e LCA ao agronegócio, conforme a estrutura legal descrita na apostila.','168','titulos_bancarios'),
('O que o FGC protege e como se aplica o limite?','Segundo a apostila (edição janeiro/2026), a garantia ordinária cobre produtos elegíveis até R$ 250 mil por CPF/CNPJ por instituição ou conglomerado, sujeita ao teto global de R$ 1 milhão a cada quatro anos.','177','fgc garantias'),
('Como o FGCoop se relaciona com depósitos em cooperativas?','É mecanismo garantidor de créditos elegíveis mantidos em cooperativas associadas, com cobertura e limites definidos pelo regulamento aplicável, conforme apresentados na apostila.','180','fgcoop garantias'),
('Qual risco permanece em uma debênture?','O investidor permanece exposto ao risco de crédito da companhia emissora, além de riscos de mercado e liquidez. Garantias da emissão não eliminam esses riscos.','182','titulos_corporativos debenture'),
])
add(11,[
('O que é um COE?','Certificado de Operações Estruturadas que combina elementos de renda fixa e derivativos em uma estrutura com cenários de retorno definidos no documento de informações essenciais.','187','coe'),
('Por que o investidor deve ler o DIE de um COE?','O DIE descreve cenários, riscos, custos, vencimento, condições de saída e eventual proteção do capital. A proteção, quando existe, depende do cumprimento das condições e do risco do emissor.','187','coe riscos'),
('Como funciona a tributação de renda fixa segundo a apostila?','Segundo a apostila (edição janeiro/2026), o IR segue tabela regressiva por prazo para aplicações tributáveis: 22,5% até 180 dias; 20% de 181 a 360; 17,5% de 361 a 720; e 15% acima de 720 dias.','189','tributacao renda_fixa'),
('Como o IOF afeta resgates de renda fixa no início da aplicação?','Segundo a apostila (edição janeiro/2026), o IOF regressivo pode incidir sobre rendimentos em resgates nos primeiros 30 dias, reduzindo-se até zero no 30º dia.','189','tributacao iof'),
])
add(12,[
('O que distingue IPO de follow-on?','IPO é a primeira abertura de capital com oferta de ações; follow-on é nova oferta por companhia já listada.','192','oferta_publica ipo'),
('Qual é a diferença entre oferta primária e secundária?','Na primária, a companhia emite ações e recebe os recursos. Na secundária, acionistas vendem ações existentes e recebem o valor da venda.','194','oferta_publica'),
('O que significa governança corporativa?','Conjunto de práticas e regras que orienta direção, monitoramento e controle da companhia, buscando transparência e equilíbrio de direitos entre interessados.','204','governanca'),
('O que é uma ação ordinária?','Ação que, em regra, confere direito de voto nas deliberações da companhia, além de direitos econômicos previstos em lei e no estatuto.','208','acoes'),
('Como diferenciar dividendos de juros sobre capital próprio?','Dividendos são parcela do lucro distribuída aos acionistas; JCP também remunera acionistas, mas recebe tratamento tributário distinto. Segundo a apostila (edição janeiro/2026), há retenção de IR na fonte de 17,5% sobre JCP.','212,231','acoes tributacao'),
])
add(13,[
('O que representa um índice de ações?','Uma carteira teórica que resume o desempenho de um conjunto definido de ativos segundo metodologia própria. Não é, por si só, um investimento diretamente detido.','221','indices'),
('O que o Ibovespa procura representar?','O desempenho médio das ações de maior negociabilidade e representatividade do mercado acionário brasileiro, segundo critérios e metodologia do índice.','223','indices ibovespa'),
('Como a apostila caracteriza a tributação de operações comuns e day trade em ações?','Segundo a apostila (edição janeiro/2026), operações comuns e day trade têm alíquotas e apuração distintas; o investidor deve separar resultados, compensar prejuízos conforme as regras e recolher o imposto devido.','230','tributacao renda_variavel'),
('Como funciona a isenção mensal de IR em vendas de ações no mercado à vista?','Segundo a apostila (edição janeiro/2026), há isenção para pessoa física em vendas mensais de ações até o limite indicado no material, restrita às operações elegíveis e sem incluir day trade.','231','tributacao renda_variavel'),
])
add(14,[
('O que é um fundo de investimento?','Uma comunhão de recursos organizada como condomínio, destinada à aplicação coletiva em ativos conforme política de investimento e regulamento.','236','fundos estrutura'),
('Como classes abertas e fechadas segregam direitos e patrimônio no regulamento?','Cada classe tem patrimônio segregado e responsabilidades próprias; pode ser aberta, com resgate previsto, ou fechada, sem resgate de cotas. Subclasses distinguem público-alvo, prazos, condições e taxas.','239','fundos cvm175'),
('O que significa responsabilidade limitada dos cotistas?','A responsabilidade do cotista por obrigações do fundo fica limitada ao valor por ele subscrito, conforme a previsão adotada nos documentos do fundo.','255','fundos riscos'),
('O que é segregação patrimonial entre classes?','Ativos e obrigações de uma classe ficam vinculados a essa classe, sem se confundirem com os de outras classes do mesmo fundo, nos termos da estrutura regulatória.','239','fundos cvm175'),
('Como distinguir gestão ativa de gestão passiva?','Gestão ativa busca superar um referencial por decisões de carteira; gestão passiva procura acompanhar um índice ou estratégia de referência.','252','fundos estrategias'),
])
add(15,[
('Qual é a função do administrador fiduciário?','Constitui e mantém o funcionamento do fundo e responde pelas atividades administrativas e deveres fiduciários que lhe cabem na regulamentação.','258','fundos participantes'),
('Qual é a função do gestor?','Toma decisões de investimento e desinvestimento da carteira dentro da política e dos limites do fundo, buscando cumprir seus objetivos.','259','fundos participantes'),
('Para que serve a assembleia de cotistas?','Delibera sobre matérias relevantes do fundo, como alterações de regulamento e substituição de prestadores, conforme regras de convocação, quórum e competência.','256','fundos assembleia'),
('Como a taxa de administração difere da taxa de performance?','A taxa de administração remunera serviços de administração e gestão. A taxa de performance, quando prevista, remunera desempenho que supera o parâmetro e as condições definidos no regulamento.','266','fundos taxas'),
('O que é um FIF?','Fundo de Investimento Financeiro, categoria que reúne fundos com carteiras financeiras submetidas às regras e limites próprios descritos na regulamentação.','272','fif'),
('O que caracteriza um fundo cambial?','Mantém exposição relevante a variação de moeda estrangeira ou cupom cambial, conforme os limites regulatórios e a política do fundo.','276','fif'),
])
add(16,[
('O que é um FII?','Fundo fechado que investe em ativos ligados ao setor imobiliário, como imóveis, recebíveis imobiliários ou cotas de outros fundos, conforme sua política.','281','fii'),
('Como cotas de FII podem ser negociadas?','Em geral, cotas de fundos listados podem ser negociadas em mercado secundário, e seu preço pode variar com oferta, demanda, ativos e condições de mercado.','282','fii liquidez'),
('Quando rendimentos de FII podem ser isentos para pessoa física?','Segundo a apostila (edição janeiro/2026), a isenção depende de requisitos legais relativos ao cotista, à negociação das cotas e à composição/quantidade de cotistas. Não se aplica automaticamente a todo rendimento ou ganho de venda.','283','fii tributacao'),
])
add(17,[
('O que ocorre na fase de diferimento de um plano de previdência?','É a fase de acumulação, quando o participante realiza contribuições e os recursos são investidos antes do início do recebimento do benefício.','288','previdencia diferimento'),
('O que ocorre na fase de benefício?','O participante passa a receber renda ou resgates conforme a modalidade contratada; regras de reversibilidade, prazo e saldo dependem do plano e da opção escolhida.','296','previdencia beneficio'),
('Qual é a principal diferença tributária entre PGBL e VGBL no resgate?','Segundo a apostila (edição janeiro/2026), no PGBL o IR incide sobre o valor total resgatado ou recebido; no VGBL incide sobre os rendimentos.','303','previdencia pgbl vgbl'),
('Para quem o PGBL pode ser mais adequado na declaração?','Em geral, para quem usa declaração completa, contribui para regime oficial e atende aos limites de dedução apresentados na apostila (edição janeiro/2026). A dedução reduz a base agora, com tributação posterior prevista.','304','previdencia pgbl'),
('Para quem o VGBL pode ser mais adequado?','Pode ser adequado a quem usa declaração simplificada, não aproveita a dedução do PGBL ou investe além do limite dedutível, pois a tributação recai sobre rendimentos, segundo a apostila (edição janeiro/2026).','305','previdencia vgbl'),
])
add(18,[
('Como os regimes progressivo e regressivo de previdência diferem?','Segundo a apostila (edição janeiro/2026), o progressivo usa tabela associada à renda tributável e pode envolver ajuste anual; o regressivo reduz alíquotas conforme o prazo de acumulação de cada contribuição.','308','previdencia tributacao'),
('Por que o prazo de cada contribuição importa no regime regressivo?','Porque a alíquota é determinada pelo tempo de permanência de cada aporte, não simplesmente pela idade do plano ou pela data do primeiro depósito.','309','previdencia regressivo'),
('O que caracteriza crédito consignado?','Empréstimo com parcelas descontadas diretamente de salário, benefício ou remuneração elegível, reduzindo risco de inadimplência, mas comprometendo renda futura.','318','credito consignado'),
('Como funciona o crédito rotativo do cartão?','É financiamento do saldo não pago integralmente na fatura. Em geral tem custo elevado; a apostila recomenda evitar seu uso recorrente e comparar alternativas de liquidação.','317','credito cartao'),
])
add(21,[
('Que objetivos pode financiar o crédito imobiliário?','Pode financiar compra, construção, reforma ou melhoria estrutural de imóvel, com valores elevados e prazo longo; as garantias e condições dependem da operação.','329','credito_imobiliario sac'),
('O que é consórcio?','Grupo de participantes contribui para formar um fundo comum, do qual os créditos são atribuídos por sorteio ou lance, conforme contrato. Não é empréstimo com liberação imediata garantida.','331','consorcio'),
('O que significa ser contemplado em um consórcio?','É obter o direito de usar a carta de crédito conforme regras do grupo, após sorteio ou lance vencedor; a contemplação não elimina obrigações contratuais ainda devidas.','332','consorcio'),
('Qual é a função do Pix no sistema de pagamentos?','Permite transferências e pagamentos eletrônicos em tempo real, com disponibilidade contínua segundo o arranjo descrito na apostila.','333','servicos_bancarios pix'),
('Como diferenciar depósito à vista de depósito a prazo?','Depósito à vista tem disponibilidade para movimentação pelo cliente; depósito a prazo fica aplicado por prazo/condições pactuados e pode ter restrição ou custo para resgate antecipado.','335','servicos_bancarios depositos'),
])
add(22,[
('O que é prêmio de seguro?','É o valor pago pelo segurado ou estipulante à seguradora para contratar a cobertura. Seu cálculo considera risco, coberturas e condições do contrato.','338','seguros'),
('O que é franquia em um seguro?','É a parcela do prejuízo que permanece a cargo do segurado em eventos cobertos, quando prevista no contrato.','338','seguros franquia'),
('Qual é a diferença entre seguradora e corretora?','A seguradora assume os riscos cobertos e paga indenizações conforme o contrato. A corretora intermedeia a contratação e orienta o cliente, sem assumir o risco segurado.','339','seguros participantes'),
('Por que revisar exclusões e carências antes de contratar?','Elas delimitam quando a cobertura não opera ou só começa após certo prazo. O cliente precisa comparar essas condições com sua necessidade de proteção.','340','seguros cobertura'),
])
add(23,[
('Como o ciclo de vida ajuda a organizar o planejamento financeiro?','Relaciona objetivos, renda, responsabilidades e horizonte de cada fase, ajudando a priorizar acumulação, proteção e uso de recursos conforme as necessidades mudam.','349','planejamento ciclo_vida'),
('O que deve constar em um orçamento pessoal?','Fontes de renda, despesas fixas e variáveis, compromissos financeiros e metas de poupança. O registro permite comparar plano e realizado e ajustar decisões.','351','orcamento'),
('Como calcular o percentual de poupança?','Percentual de poupança = (renda líquida − despesas/consumo) ÷ renda líquida × 100. Defina o mesmo período para numerador e denominador.','353','fluxo_caixa calculo'),
('Que função cumpre o fluxo de caixa pessoal?','Registra entradas e saídas ao longo do tempo para revelar sobras, déficits e datas de maior pressão financeira.','352','fluxo_caixa'),
])
add(24,[
('O que avaliar antes de recomendar novo crédito a um cliente?','Renda recorrente, dívidas existentes, valor e prazo das parcelas, capacidade de pagamento, garantias e efeito sobre objetivos e orçamento.','354','credito capacidade'),
('Como medir o comprometimento de renda com dívidas?','Some as parcelas e obrigações financeiras do período, divida pela renda líquida recorrente do mesmo período e multiplique por 100. Avalie junto a estabilidade da renda e despesas essenciais.','355','credito calculo'),
('Quando uma dívida pode ser uma ferramenta financeira?','Quando financia um objetivo compatível com a capacidade de pagamento e o custo/benefício, sem comprometer despesas essenciais nem gerar endividamento insustentável.','357','dividas credito'),
('Qual é uma estratégia para reorganizar dívidas caras?','Mapear saldo, taxa e prazo; priorizar renegociação ou substituição de linhas de custo alto por crédito mais barato, desde que a nova operação reduza custo total e caiba no orçamento.','359','dividas'),
('Por que a amortização antecipada deve ser comparada ao investimento alternativo?','A economia de juros da dívida deve ser confrontada com o retorno líquido, risco, liquidez e impostos da aplicação alternativa, além da preservação de reserva adequada.','364','credito amortizacao'),
])
add(25,[
('Como calcular o patrimônio líquido pessoal?','Patrimônio líquido = total de ativos − total de passivos, em uma data de referência.','376','balanco patrimonio'),
('O que indica a liquidez corrente pessoal?','Ativo circulante dividido por passivo circulante. Valores maiores indicam mais ativos de curto prazo em relação a obrigações de curto prazo, sem garantir que os ativos sejam imediatamente realizáveis.','383','indicadores liquidez'),
('Como diferem endividamento sobre ativos e dívida sobre patrimônio líquido?','Passivos ÷ ativos mostra a parcela dos ativos financiada por dívidas. Passivos ÷ patrimônio líquido compara as dívidas ao capital próprio. Os denominadores são diferentes; confira qual indicador a questão pede.','379,380','indicadores endividamento'),
('O que é cobertura de despesas por reserva?','É o número de períodos de despesas essenciais que os recursos líquidos reservados conseguem cobrir: reserva disponível ÷ despesa essencial do período.','383','indicadores reserva'),
('Por que separar ativos geradores de renda dos bens de uso?','A separação mostra quais ativos podem produzir fluxo financeiro e quais atendem ao consumo ou uso pessoal, apoiando avaliação de liquidez, renda e planejamento.','381','balanco ativos'),
])
add(26,[
('O que é rendimento tributável no IRPF?','É rendimento que compõe a base tributável conforme a classificação fiscal, como salários e certas receitas financeiras. A natureza da fonte e a regra específica definem o tratamento.','388','irpf rendimentos'),
('Qual é a diferença entre ganho de capital e renda periódica?','Ganho de capital é o resultado positivo na alienação de um bem ou direito em relação ao custo fiscal. Renda periódica decorre de pagamentos ou rendimentos recebidos ao longo do tempo.','387','irpf ganho_capital'),
('O que distingue os modelos completo e simplificado de declaração?','O completo permite deduções legais comprovadas; o simplificado aplica desconto padrão limitado. A escolha depende do cálculo que resulta em menor imposto ou maior restituição.','389','irpf declaracao'),
('Como a apostila distingue investidor qualificado de profissional?','Segundo a apostila (edição janeiro/2026), são categorias definidas por critérios regulatórios de patrimônio financeiro, certificação ou condição institucional, que ampliam o conjunto de produtos acessíveis.','392','investidores qualificacao'),
])
add(27,[
('Que princípios devem orientar a conduta ética no mercado financeiro?','Honestidade, equidade, diligência, independência, transparência, competência e preservação do sigilo, conforme o dever aplicável ao profissional.','394','etica'),
('O que significa suitability?','Processo de verificar se produto, serviço ou operação é compatível com objetivos, situação financeira e conhecimento/experiência do cliente, além de seu perfil de risco.','395','suitability api'),
('O que fazer quando o cliente insiste em operação incompatível com seu perfil?','Explicar a incompatibilidade e os riscos, seguir os procedimentos de alerta e registro previstos e não apresentar a operação como adequada. As regras específicas determinam quando a execução pode ocorrer.','397','suitability'),
('Como a escuta ativa melhora o atendimento?','Ajuda a identificar objetivos, restrições e compreensão do cliente antes de propor soluções, permitindo explicar alternativas em linguagem adequada e confirmar entendimento.','398','atendimento'),
])
add(28,[
('Qual é o objetivo do KYC?','Conhecer identidade, atividade, capacidade financeira, origem de recursos e propósito do relacionamento para avaliar riscos e detectar inconsistências.','400','kyc'),
('Quais são as três etapas clássicas da lavagem de dinheiro?','Colocação, ocultação e integração. Primeiro os recursos entram no sistema, depois se dissimula sua origem e, por fim, retornam à economia com aparência lícita.','402','pldft'),
('O que caracteriza uma operação suspeita para fins de PLDFT?','Uma operação incompatível com perfil, atividade, capacidade financeira ou padrão transacional do cliente, ou que apresente sinais previstos nas regras. A suspeita deve ser analisada e tratada conforme procedimentos.','405','pldft monitoramento'),
('Qual é a função do Coaf?','Recebe, examina e identifica ocorrências suspeitas de atividades ilícitas e produz inteligência financeira, além das atribuições de supervisão descritas para setores obrigados.','409','pldft coaf'),
('Como pessoas expostas politicamente afetam a diligência devida?','A condição exige atenção reforçada e monitoramento conforme regras aplicáveis, incluindo análise de origem de recursos e pessoas relacionadas; não significa, por si só, que haja ilícito.','411','pldft pep'),
])
add(29,[
('O que é dado pessoal segundo a LGPD?','Informação relacionada a pessoa natural identificada ou identificável. Dado pessoal sensível é categoria específica sujeita a proteção reforçada.','412','lgpd dados'),
('Quais princípios da LGPD orientam o tratamento de dados de clientes?','Finalidade, adequação, necessidade, transparência, segurança, prevenção, não discriminação e responsabilização, entre outros princípios legais.','413','lgpd principios'),
('O que caracteriza insider trading?','Negociar valores mobiliários usando informação relevante ainda não divulgada ao mercado, ou repassá-la indevidamente, obtendo vantagem ou evitando perda.','415','crimes mercado insider'),
('O que é spoofing no mercado?','Inserir ordens sem intenção real de execução para criar falsa impressão de oferta ou demanda e induzir outros participantes.','417','crimes mercado spoofing'),
('O que caracteriza front running?','Negociar por conta própria antes de executar ordem relevante de cliente, aproveitando-se da informação sobre a ordem e prejudicando o cliente.','419','crimes mercado front_running'),
])
add(31,[
('O que significam os pilares ambiental, social e de governança em ESG?','Ambiental trata de impactos e riscos sobre recursos e clima; social abrange relações com trabalhadores, clientes e comunidades; governança examina direção, controles, ética e direitos.','423','esg pilares'),
('O que é engajamento acionário em estratégia ESG?','Uso ativo de direitos de acionista para dialogar com a companhia e influenciar suas práticas e decisões socioambientais ou de governança.','425','esg engajamento'),
('Como um fundo pode integrar fatores ESG à análise de investimentos?','Pode incorporar riscos e oportunidades ESG à seleção e gestão dos ativos, com critérios, dados e objetivos definidos e divulgados ao investidor.','426','esg investimentos'),
('Qual é a diferença entre risco climático físico e de transição?','Risco físico decorre de eventos e mudanças climáticas que afetam ativos e operações. Risco de transição surge de mudanças regulatórias, tecnológicas, de mercado ou reputacionais ligadas à economia de baixo carbono.','429','esg risco_climatico'),
('O que caracteriza um título verde?','Instrumento cujos recursos são destinados a projetos ambientais elegíveis e cujo uso e reporte seguem critérios divulgados na emissão.','430','esg titulos'),
])
add(32,[
('Como funciona um blockchain?','É um registro distribuído em que transações são agrupadas em blocos ligados criptograficamente; participantes validam atualizações segundo regras de consenso da rede.','434','blockchain'),
('Como diferenciar blockchain permissionada de pública?','Em rede pública, participação e validação seguem regras abertas; em rede permissionada, acesso ou validação são restritos a participantes autorizados.','434','blockchain redes'),
('O que é tokenização?','Representação digital de direitos ou ativos por tokens registrados em uma infraestrutura tecnológica. O token não elimina direitos legais, riscos do ativo ou necessidade de regras de custódia.','435','tokenizacao'),
('O que é um criptoativo?','Ativo digital que pode ser transferido e registrado por tecnologias criptográficas e de registro distribuído. Suas características, direitos e riscos variam entre projetos.','437','criptoativos'),
('Qual é a diferença entre hot wallet e cold wallet?','Hot wallet fica conectada à internet e facilita transações, mas amplia exposição online. Cold wallet mantém chaves fora de conexão contínua, reduzindo certos riscos e exigindo cuidado físico e operacional.','438','criptoativos custodia'),
('O que é um smart contract?','Código implantado em blockchain que executa automaticamente regras e ações quando condições programadas são satisfeitas. Erros de código e dados externos podem produzir resultados indesejados.','440','smart_contracts'),
('O que é uma stablecoin?','Criptoativo concebido para manter valor relativamente estável em relação a um ativo de referência. A estabilidade depende de reservas, mecanismos e governança, portanto não é garantida pelo nome.','445','criptoativos stablecoin'),
])
add(33,[
('O que é uma fintech?','Empresa que usa tecnologia para oferecer ou apoiar serviços financeiros, podendo atuar em pagamentos, crédito, investimentos ou outras atividades sujeitas a regras específicas.','448','fintechs'),
('O que diferencia SCD de SEP na concessão de crédito?','Segundo a apostila (edição janeiro/2026), a SCD realiza operações de crédito com recursos próprios dentro do modelo autorizado; a SEP conecta credores e devedores em empréstimos entre pessoas, sem usar capital próprio para emprestar.','452','fintechs credito'),
('Como funciona o sandbox regulatório?','Permite testar inovação em ambiente delimitado e supervisionado, com participantes, prazos, escopo e salvaguardas definidos pelo regulador.','450','fintechs sandbox'),
('O que é Open Finance?','Compartilhamento padronizado de dados e serviços financeiros entre instituições autorizadas, mediante consentimento do cliente e controles de segurança previstos no arranjo.','455','open_finance'),
('O que acrescentam Open Investment e Open Insurance?','Ampliam o compartilhamento consentido de dados e serviços para os segmentos de investimentos e seguros, permitindo integração e comparação entre provedores conforme o escopo autorizado.','457','open_investment open_insurance'),
('Para que serve um prompt em uma ferramenta de IA generativa?','É a instrução que delimita tarefa, contexto, formato e critérios da resposta. Instruções claras e contexto suficiente tendem a produzir saídas mais úteis, que ainda precisam de verificação.','460','ia prompt'),
('Como a apostila descreve o uso de modelos de IA para risco de crédito?','A apostila apresenta modelos para prever retornos ou identificar probabilidade de inadimplência. A saída funciona como ferramenta de análise, que precisa ser interpretada junto ao contexto do cliente.','461','ia governanca'),
])
add(3,[
('O que caracteriza risco operacional?','Perdas decorrentes de falhas, inadequação ou deficiência de processos, pessoas e sistemas, ou de eventos externos.','50','riscos operacional'),
('Como risco social pode afetar uma instituição financeira?','Eventos como assédio, discriminação ou violações de direitos podem gerar perdas, sanções, danos reputacionais e impactos sobre pessoas e operações.','47','riscos social'),
('Como risco ambiental pode gerar perdas financeiras?','Eventos ambientais podem afetar ativos, operações, garantias e capacidade de pagamento de clientes, além de gerar custos legais e reputacionais.','48','riscos ambiental'),
('Como mitigar risco de liquidez de uma carteira?','Manter ativos negociáveis e compatibilizar prazos dos ativos com necessidades de caixa; diversificar fontes de liquidez e avaliar cenários de resgate.','46','riscos liquidez'),
])
add(7,[
('O que é o fluxo circular da renda?','Modelo que mostra a interação entre famílias, empresas, governo e demais setores: famílias oferecem fatores e consomem; empresas produzem e remuneram fatores.','118','pib economia'),
('Como calcular o PIB pela ótica da despesa?','Somam-se consumo das famílias, investimento, gastos do governo e exportações líquidas: PIB = C + I + G + (X−M).','124','pib formula'),
('Como uma política fiscal expansionista pode afetar a demanda agregada?','Aumento de gastos ou redução de tributos tende a elevar a demanda no curto prazo, mas pode ampliar déficit e pressão inflacionária conforme o contexto.','139','politica fiscal'),
('O que é elasticidade-preço da demanda?','Mede a variação percentual da quantidade demandada diante de uma variação percentual do preço. Quanto maior o valor absoluto, maior a sensibilidade da quantidade ao preço.','122','economia elasticidade'),
])
add(10,[
('O que é uma Letra Financeira?','Título de captação bancária de prazo mais longo, com condições de remuneração e resgate previstas na emissão; deve-se avaliar liquidez, emissor e eventual ausência de garantia ordinária.','170','titulos_bancarios lf'),
('O que diferencia uma debênture incentivada de uma debênture comum para a pessoa física?','Segundo a apostila (edição janeiro/2026), a incentivada financia projetos prioritários e pode ter tratamento tributário favorecido para pessoa física, conforme requisitos legais. O risco de crédito do emissor permanece.','182','titulos_corporativos tributacao'),
])
add(12,[
('O que é tag along?','Mecanismo que estende a acionistas minoritários condições de venda de ações em caso de alienação de controle, conforme percentual e regras aplicáveis.','203','governanca tag_along'),
('O que é direito de subscrição?','Preferência de acionistas para adquirir novas ações em aumento de capital, na proporção e no prazo definidos, preservando sua participação se exercerem o direito.','210','acoes subscricao'),
('Como diferenciar análise fundamentalista de análise técnica?','A fundamentalista avalia fundamentos econômicos, financeiros e perspectivas do emissor. A técnica analisa padrões de preços e volumes para estudar comportamento de mercado.','218','acoes analise'),
])
add(14,[
('O que é um fundo aberto?','Fundo em que, conforme regulamento, cotistas podem solicitar aplicações e resgates; a liquidez depende dos prazos e condições estabelecidos.','247','fundos aberto'),
('O que significa come-cotas?','Segundo a apostila (edição janeiro/2026), é antecipação periódica do IR em determinados fundos, realizada por redução de cotas, observadas as exceções e regras tributárias de cada classe.','252','fundos tributacao'),
])
add(16,[
('Como diferenciar FII de imóvel mantido diretamente?','A cota de FII representa participação em carteira coletiva e pode ter negociação e distribuição de rendimentos conforme o fundo. Não confere propriedade direta de um imóvel específico ao cotista.','281','fii'),
])
add(18,[
('O que é crédito pessoal não consignado?','Empréstimo em que o pagamento não é descontado automaticamente da remuneração, normalmente com análise de crédito e condições de taxa e prazo definidas pelo credor.','315','credito emprestimo'),
])
add(21,[
('O que é alienação fiduciária em financiamento imobiliário?','Garantia em que a propriedade resolúvel do bem é transferida ao credor até a quitação, enquanto o devedor mantém a posse direta conforme o contrato.','327','credito_imobiliario garantia'),
('O que é subadquirente em pagamentos?','Prestador que habilita estabelecimentos a aceitar pagamentos eletrônicos, conectando o lojista a credenciadores e arranjos de pagamento e facilitando captura e liquidação.','336','servicos_bancarios pagamentos'),
])
add(22,[
('O que é indenização de seguro?','Valor ou prestação que a seguradora paga ao beneficiário ou segurado quando ocorre evento coberto e são atendidas as condições contratuais.','340','seguros indenizacao'),
])
add(25,[
('Como interpretar um índice de endividamento de 40% dos ativos?','Se calculado como passivos/ativos, indica que 40% do valor dos ativos está financiado por obrigações; o restante corresponde ao patrimônio líquido, sob essa identidade contábil.','379','indicadores endividamento'),
])
add(28,[
('O que significa abordagem baseada em risco na PLDFT?','A instituição ajusta intensidade de identificação, diligência e monitoramento ao risco do cliente, produto, canal, operação e localização, mantendo controles proporcionais.','400','pldft risco'),
])
add(31,[
('O que diferencia investimento sustentável de simples rotulagem ESG?','Uma estratégia sustentável explicita objetivo, critérios, processo de seleção e monitoramento de resultados. O rótulo isolado não demonstra impacto nem qualidade da análise.','430','esg investimentos'),
('O que é greenwashing?','Apresentar produto, empresa ou atividade como ambientalmente sustentável sem evidência ou consistência suficiente entre alegações, critérios e práticas.','431','esg greenwashing'),
('O que são títulos sociais e sustentáveis?','Títulos sociais destinam recursos a projetos com benefícios sociais; títulos sustentáveis combinam usos ambientais e sociais, com critérios e prestação de contas da emissão.','430','esg titulos'),
])
add(32,[
('O que é um token não fungível (NFT)?','Token que representa unidade digital singular e não intercambiável em relação de um para um com outro token. A posse do token não garante, por si só, direitos autorais sobre a obra associada.','444','criptoativos nft'),
('O que é uma DAO?','Organização que coordena decisões por regras e mecanismos digitais, frequentemente com votação de detentores de tokens de governança; sua estrutura não elimina riscos jurídicos e técnicos.','439','blockchain dao'),
('Como um ETF de Bitcoin difere da custódia direta de criptoativo?','O ETF oferece exposição por meio de cotas de fundo negociadas no mercado tradicional, enquanto a custódia direta exige gerir chaves e carteira. Os riscos e direitos são diferentes.','447','criptoativos etf'),
('O que representa o Drex na apostila?','Segundo a apostila (edição janeiro/2026), é a representação digital do real em infraestrutura digital, com paridade 1:1 e usos previstos para liquidação de serviços financeiros.','448','criptoativos drex'),
('O que é renda fixa digital?','Representação ou distribuição digital de um título de renda fixa tradicional, com prazo e remuneração definidos. A forma digital não elimina risco do emissor nem substitui análise contratual.','446','criptoativos renda_fixa_digital'),
])
add(33,[
('O que faz um credenciador?','Habilita estabelecimentos comerciais a aceitar instrumentos de pagamento e participa da captura e liquidação das transações no arranjo.','453','pagamentos credenciador'),
('Como deve ocorrer o compartilhamento de dados no Open Finance?','Com consentimento livre, informado e específico do cliente, para finalidades e prazos determinados, por instituições participantes autorizadas e com controles de segurança.','455','open_finance consentimento'),
])

add(11,[
('Quais são as alíquotas regressivas do IR sobre renda fixa segundo a apostila?','Segundo a apostila (edição janeiro/2026): até 180 dias, 22,5%; de 181 a 360 dias, 20%; de 361 a 720 dias, 17,5%; acima de 720 dias, 15%.','189','tributacao ir'),
('Qual é a base de cálculo do IR em renda fixa segundo a apostila?','Segundo a apostila (edição janeiro/2026), a base é a diferença positiva entre o valor de alienação, líquido do IOF quando aplicável, e o valor aplicado. O imposto é retido na fonte e tratado como definitivo no material.','189','tributacao ir'),
('Quando ocorre a incidência de IR sobre cupom de título de renda fixa?','No pagamento ou crédito do cupom, contando o prazo entre a aquisição e o recebimento para determinar a alíquota regressiva, segundo a apostila (edição janeiro/2026).','189','tributacao ir cupons'),
('Como o IOF de renda fixa incide antes de 30 dias?','Segundo a apostila (edição janeiro/2026), incide sobre o rendimento, não sobre o principal, com alíquota regressiva diária; no 30º dia a alíquota chega a zero.','189','tributacao iof'),
('Qual é a alíquota de IOF indicada para resgate no 15º dia?','Segundo a apostila (edição janeiro/2026), a alíquota é 50% do rendimento. Em ganho de R$ 100,00, o IOF é R$ 50,00.','190','tributacao iof'),
('Como calcular IR e IOF para R$ 100 de rendimento resgatado no 15º dia?','Segundo o exemplo da apostila (edição janeiro/2026): IOF = 50%×R$100 = R$50; base líquida = R$50; IR = 22,5%×R$50 = R$11,25. Sobre aplicação de R$100.000 com saldo bruto de R$100.100, o líquido após tributos é R$100.038,75.','191','tributacao calculo'),
('Quais investimentos de renda fixa a apostila lista como isentos de IR para pessoa física?','Segundo a apostila (edição janeiro/2026), a lista inclui poupança, debêntures incentivadas, CRI, LH, LCI, LCA, CRA e CPR. O ganho de capital na alienação ou cessão desses títulos não fica isento pela mesma regra.','189','tributacao isencao'),
('O COE conta com cobertura do FGC?','Não. A apostila informa que COE não conta com garantia do FGC; resgate antecipado pode ocorrer sujeito à marcação a mercado e sem garantia do principal.','188','coe fgc riscos'),
])
add(15,[
('Quais decisões cabem à assembleia geral de cotistas?','Pode aprovar demonstrações contábeis, substituição de administrador ou gestor, emissão de cotas de classe fechada, reorganização ou liquidação do fundo, alterações do regulamento e medidas sobre patrimônio líquido negativo/insolvência, conforme a apostila.','256','fundos assembleia'),
('Qual é o prazo de convocação de assembleia e o prazo de divulgação das decisões?','Segundo a apostila (edição janeiro/2026), convocação com pelo menos 10 dias de antecedência; resumo das decisões disponível em até 30 dias após a reunião.','256','fundos assembleia'),
('Quem pode convocar assembleia de cotistas segundo a apostila?','Administrador, gestor ou cotistas que representem pelo menos 5% do patrimônio líquido/cotas, conforme o trecho aplicável. A assembleia anual deve tratar das demonstrações contábeis.','257','fundos assembleia'),
('Qual é a função do custodiante de um fundo?','É responsável pela liquidação física e financeira dos ativos da carteira e por funções de custódia, mantendo os ativos sob controle e registro conforme a regulamentação.','260','fundos participantes'),
('Qual é a função do distribuidor de cotas?','Oferta e comercialização de cotas, contato com o investidor, cadastro, coleta de informações, prevenção à lavagem de dinheiro e verificação de suitability.','260','fundos participantes distribuicao'),
('O que caracteriza investimento por conta e ordem?','O investidor escolhe o produto, mas uma instituição intermediária executa e mantém registros da aplicação em seu nome operacional, assumindo deveres de identificação, documentação, comunicação e controles.','262','fundos conta_ordem'),
('Para que serve o side pocket em um fundo?','Separa ativos ilíquidos em nova classe fechada ou subclasse para evitar venda forçada em condições desfavoráveis e reduzir transferência de valor entre cotistas.','264','fundos side_pocket'),
('Como se calcula a provisão diária de uma taxa de administração de 0,6% a.a. sobre PL de R$ 12 milhões?','Pela convenção apresentada: PL × (taxa anual/252) = R$12.000.000 × (0,006/252) = R$285,71 por dia útil, aproximadamente. A taxa incide independentemente de rentabilidade.','266','fundos taxas calculo'),
('Quando a taxa de performance é cobrada?','Quando o fundo supera o benchmark previsto, sobre a parcela excedente e respeitando linha d’água, periodicidade e regras da classe. O referencial deve ser compatível com a política de investimento.','267','fundos performance'),
('O que impede a linha d’água na taxa de performance?','Ela impede cobrar performance enquanto a cota apenas recupera perdas anteriores; só há cobrança quando supera o maior valor de referência ajustado por distribuições, conforme a apostila.','267','fundos linha_dagua'),
('Como funcionam taxas de ingresso e saída?','A taxa de ingresso é cobrada na entrada, como percentual do aporte. A taxa de saída é cobrada no resgate e pode variar com o prazo de permanência.','269','fundos taxas'),
('Como se altera o valor das taxas de administração, performance, entrada e saída?','Segundo a apostila (edição janeiro/2026), aumento exige aprovação em assembleia. A redução pode ser feita pelo administrador, com comunicação aos cotistas e à CVM.','269','fundos taxas'),
('Quais limites definem um fundo de renda fixa de curto prazo?','Segundo a apostila (edição janeiro/2026), títulos da carteira têm prazo máximo de 375 dias e prazo médio inferior a 60 dias; derivativos são permitidos para hedge.','274','fif renda_fixa'),
('Qual percentual mínimo de carteira caracteriza um fundo de renda fixa simples?','Segundo a apostila (edição janeiro/2026), no mínimo 95% do patrimônio líquido deve ficar em títulos públicos ou renda fixa de instituições financeiras de alta classificação de risco; derivativos ficam restritos a hedge.','275','fif renda_fixa'),
('Quais limites descrevem um fundo de renda fixa referenciado?','Segundo a apostila (edição janeiro/2026), no mínimo 80% em ativos de baixo risco alinhados ao índice e 95% acompanhando direta ou indiretamente o índice de referência; derivativos para hedge até as posições à vista.','276','fif renda_fixa'),
('Que concentração por emissor é citada para fundo de renda fixa de dívida externa?','Segundo a apostila (edição janeiro/2026), o total emitido ou coobrigado por uma mesma entidade não pode exceder 10% do patrimônio líquido; a carteira mantém ao menos 80% em títulos de dívida externa.','277','fif divida_externa'),
('Qual percentual mínimo em ações caracteriza um FIA?','Segundo a apostila (edição janeiro/2026), pelo menos 67% do patrimônio líquido deve estar em ativos relacionados ao mercado de ações, como ações, ETFs de ações, BDRs elegíveis e cotas de outros FIAs.','278','fif fia'),
('Qual exposição mínima caracteriza um fundo cambial?','Segundo a apostila (edição janeiro/2026), a carteira deve manter ao menos 80% vinculados ao fator de risco cambial. O fundo pode servir a exposição, hedge ou especulação cambial.','280','fif cambial'),
])

add(4,[
('Por que taxa e prazo precisam usar a mesma periodicidade?','A taxa i e o número de períodos n da fórmula composta precisam se referir à mesma unidade. Se a taxa é mensal e o prazo é 6 meses, use n=6; para prazo em dias, converta conforme a convenção indicada.','79','juros compostos hp12c'),
('Qual é a taxa efetiva anual equivalente a 4% ao mês?','(1,04)^12−1 = 60,10% ao ano, aproximadamente. A conversão efetiva capitaliza mês a mês, não multiplica 4% por 12.','75','taxas equivalentes calculo'),
('Como diferem taxas proporcionais e equivalentes?','Taxas proporcionais variam linearmente com o prazo, como 10% ao mês × 2 = 20% em dois meses sob juros simples. Taxas equivalentes produzem o mesmo montante sob capitalização composta: (1,10)^2−1 = 21%.','76','taxas proporcionais'),
('Como calcular retorno acumulado de +5%, depois −4%?','Multiplique os fatores: 1,05×0,96−1 = 0,8%. Retornos sucessivos não se somam diretamente.','77','rentabilidade acumulada calculo'),
('Como comparar uma taxa bruta de fundo com uma taxa líquida?','Desconte tributos e encargos aplicáveis da rentabilidade bruta antes de comparar com produto isento ou já líquido. No exemplo da apostila, 0,75% bruto com IR de 22,5% sobre o rendimento resulta em cerca de 0,5812% líquido.','78','rentabilidade tributacao'),
('Quanto capital é necessário para gerar renda perpétua de R$ 5.000 por mês a 0,5% ao mês?','Capital = renda mensal/taxa mensal = R$ 5.000/0,005 = R$ 1.000.000, supondo taxa constante e preservação do principal.','79','perpetuidade calculo'),
('Que cuidados tomar ao calcular valor presente e valor futuro na HP-12C?','Limpe os registros financeiros, alinhe taxa e prazo, informe entradas e saídas com sinais opostos e use PV/FV para resolver. A apostila usa a convenção exponencial.','80','hp12c tvm'),
('Qual o montante de R$ 1.500 aplicados por 6 meses a 1,4% ao mês?','FV = 1.500×(1,014)^6 = R$ 1.630,49. Com IR de 20% sobre ganho de R$130,49, o resgate líquido do exemplo é R$1.604,39.','82','juros compostos calculo'),
])
add(6,[
('Qual é o WACC aproximado de empresa com PL R$100 mi a custo de 15%, dívida R$30 mi a 10% e IR de 30%?','WACC = (100/130)×15% + (30/130)×10%×(1−30%) ≈ 13,15% a.a. O benefício fiscal reduz o custo ponderado da dívida no exemplo.','95','wacc calculo'),
('Como calcular a duration de Macaulay?','Some cada fluxo de caixa descontado multiplicado pelo período em que será recebido e divida pela soma dos valores presentes: D = Σ[t×PV(FC_t)]/ΣPV(FC_t).','96','duration formula'),
('Qual é a duration aproximada do título de R$1.000, cupom anual de 8%, vencimento em 5 anos e yield de 6%?','Recalculando os fluxos da apostila: R$80 nos anos 1 a 4 e R$1.080 no ano 5, descontados a 6% a.a., dão PV total de R$1.084,25 e soma ponderada de R$4.708,04; duration = 4.708,04/1.084,25 ≈ 4,34 anos.','97','duration calculo'),
('O que estima a duration modificada de 4,10?','A aproximação é que o preço varia cerca de −4,10% quando a taxa sobe 1 ponto percentual, ou +4,10% quando cai 1 ponto, para pequenas mudanças e mantidas as demais condições.','99','duration modificada'),
('Como imunizar uma obrigação de 5 anos com títulos de duration 3 e 8 anos?','Iguale a duration da carteira a 5 anos: 3wA+8wB=5 e wA+wB=1. Resulta em 60% no título A e 40% no B.','101','duration imunizacao calculo'),
('Como diferem desconto racional e desconto comercial simples?','Racional “por dentro” calcula juros sobre o valor atual: VP=N/(1+i×n). Comercial “por fora” calcula D=N×d×n sobre o nominal e libera N−D antes de tarifas/tributos.','102','desconto'),
('Quanto libera o desconto comercial de R$20.000 por 3 meses a 2% ao mês antes de tarifas?','Desconto = 20.000×0,02×3=R$1.200; valor líquido antes de outros custos = R$18.800. No exemplo bancário, TAC e IOF reduzem ainda mais o valor.','103','desconto calculo'),
('Como interpretar a TMA em uma decisão de investimento?','É o retorno mínimo exigido pelo investidor ou o custo de oportunidade/capital usado para comparar o projeto. Projeto com retorno abaixo da TMA não atende ao mínimo requerido.','110','investimentos tma'),
('Quando a TIR pode produzir mais de uma resposta?','Quando o fluxo de caixa muda de sinal mais de uma vez, pode haver múltiplas TIRs; por isso compare VPL à TMA e examine o perfil do fluxo.','104','investimentos tir'),
('O que a TIR modificada corrige em relação à TIR tradicional?','Explicita a taxa de reinvestimento dos fluxos positivos e pode usar taxa de financiamento para fluxos negativos, tornando a hipótese de reinvestimento mais realista.','108','investimentos mirr'),
('Qual é o VPL do fluxo −R$50.000, +R$25.000, +R$20.000 e +R$15.000 a 8%?','VPL = −50.000 + 25.000/1,08 + 20.000/(1,08)^2 + 15.000/(1,08)^3 ≈ R$2.202,41. Como é positivo, supera a TMA de 8% nas premissas do caso.','113','investimentos vpl calculo'),
])
add(3,[
('Como diferenciar risco de inadimplência e risco de degradação da qualidade de crédito?','Inadimplência é o não pagamento de uma obrigação. A deterioração da qualidade de crédito pode surgir antes, com piora de rating, indicadores financeiros ou capacidade de pagamento do devedor.','43','riscos credito'),
('O que é risco de concentração?','Perda potencial ampliada pela exposição excessiva a um mesmo emissor, setor, contraparte, região ou fator de risco; limites e diversificação ajudam a reduzir essa dependência.','44','riscos concentracao'),
('O que significa risco sistemático?','Risco ligado a fatores amplos que afetam o mercado e não é eliminado apenas pela diversificação de ativos dentro daquele mercado.','44','riscos mercado'),
])
add(7,[
('Como se diferenciam mercados monetário, de crédito e de capitais?','O monetário administra liquidez e operações de curto prazo; o de crédito intermedeia empréstimos; o de capitais canaliza recursos por valores mobiliários, com investidor assumindo risco do emissor.','120','economia mercados'),
('Como se distinguem PIB nominal e PIB real?','PIB nominal usa preços correntes do período. PIB real desconta o efeito da variação de preços para permitir comparação de volume produzido ao longo do tempo.','124','pib'),
('Qual é a diferença entre IPCA e INPC segundo a apostila?','Ambos são índices de preços calculados pelo IBGE, mas cobrem populações e cestas com recortes diferentes; IPCA é referência central do regime de metas de inflação e o INPC foca famílias de menor renda.','131','inflacao indicadores'),
('O que é inflação acumulada em doze meses?','Variação composta do índice de preços nos últimos doze meses, calculada multiplicando os fatores mensais e subtraindo 1; não é a soma simples das taxas mensais.','125','inflacao calculo'),
('Qual é o papel do Copom na definição da Selic?','O Copom decide a meta da taxa Selic em reuniões periódicas, considerando perspectivas e riscos para a inflação; a decisão busca orientar condições monetárias.','130','copom selic'),
('Como diferem política monetária expansionista e contracionista?','A expansionista busca ampliar liquidez e atividade, por exemplo reduzindo juros; a contracionista restringe condições financeiras para conter pressões inflacionárias, por exemplo elevando juros.','137','politica monetaria'),
('O que é resultado primário do setor público?','Diferença entre receitas e despesas não financeiras do governo; não inclui juros da dívida no cálculo primário, segundo a definição apresentada na apostila.','139','politica fiscal'),
])

add(9,[
('Como funciona um Tesouro Prefixado sem cupom?','O investidor compra o título por preço inferior ao valor de resgate e recebe o valor nominal no vencimento. O retorno contratado depende de manter o título até o vencimento e da solvência soberana.','156','tesouro prefixado'),
('Como o Tesouro Prefixado com juros semestrais paga o investidor?','Além do valor principal no vencimento, paga cupons periódicos. Os cupons antecipam parte dos fluxos e criam risco de reinvestimento.','158','tesouro cupons'),
('Qual é a diferença entre Tesouro IPCA+ e Tesouro IPCA+ com juros semestrais?','Ambos combinam inflação medida pelo IPCA e taxa prefixada real; o segundo antecipa cupons semestrais, enquanto o primeiro concentra o fluxo no vencimento.','161','tesouro ipca'),
('Para que foram desenhados Tesouro RendA+ e Tesouro Educa+?','Segundo a apostila, RendA+ estrutura pagamentos mensais para complementar renda na aposentadoria; Educa+ estrutura renda mensal por período determinado para custear educação.','162','tesouro rendA educa'),
])
add(10,[
('Quais instrumentos a apostila lista como cobertos pelo FGC?','Segundo a apostila (edição janeiro/2026), a lista inclui depósitos à vista e poupança, CDB/RDB, LC, LH, LCI/LCA, LCD e determinadas operações compromissadas. Elegibilidade depende das regras do fundo.','179','fgc produtos'),
('Quais instrumentos a apostila indica como não cobertos pelo FGC?','Segundo a apostila (edição janeiro/2026), incluem letras financeiras, LIG, COE, debêntures, CRI/CRA, ações, fundos de investimento e títulos públicos.','179','fgc produtos'),
('Qual é a prioridade de garantias em debêntures apresentada na apostila?','Real, flutuante, quirografária e subordinada, nessa ordem de preferência descrita no material. Garantia não elimina o risco de perda.','183','titulos_corporativos garantias'),
('Que prazo máximo a apostila atribui à nota promissória comercial?','Até 360 dias, segundo a apostila (edição janeiro/2026), salvo as exceções cumulativas indicadas para oferta com esforços restritos e agente de proteção dos titulares.','185','titulos_corporativos nota_promissoria'),
])
add(12,[
('Como o mercado primário difere do secundário para ações?','No primário, a empresa emite ações e capta novos recursos. No secundário, investidores negociam ações existentes entre si e a companhia não recebe o preço da negociação.','194','oferta_publica'),
('O que é período de reserva em um IPO?','É o período em que o investidor manifesta à corretora a quantidade ou o valor que pretende subscrever. Se a demanda supera a oferta, pode haver rateio.','201','oferta_publica ipo'),
('O que caracteriza uma ação preferencial?','Pode conferir prioridade em dividendos ou reembolso de capital, conforme a classe e o estatuto; em regra, não tem o mesmo direito de voto pleno da ação ordinária.','208','acoes'),
('Como funciona o direito de subscrição em aumento de capital?','O acionista pode adquirir novas ações em proporção à participação atual para evitar diluição. Se não exercer ou negociar o direito no prazo, sua participação relativa pode cair.','213','acoes subscricao'),
('Qual é a diferença entre split e grupamento?','Split divide cada ação em várias, reduzindo preço por ação sem alterar valor total da posição. Grupamento consolida ações, elevando preço unitário sem alterar o valor total teórico.','214','acoes'),
])
add(13,[
('Qual é a alíquota indicada pela apostila para ganho em operações comuns com ações?','Segundo a apostila (edição janeiro/2026), a alíquota é 15% sobre o ganho líquido em operações comuns, sujeita às regras de apuração e isenções descritas.','232','tributacao renda_variavel'),
('Qual é a alíquota indicada para day trade?','Segundo a apostila (edição janeiro/2026), day trade é tributado a 20%, com retenção na fonte de 1% sobre o lucro como antecipação.','230','tributacao renda_variavel'),
('Como se compensam prejuízos de day trade?','Segundo a apostila (edição janeiro/2026), prejuízos de day trade compensam ganhos de day trade; não se misturam livremente com prejuízos de operações comuns.','235','tributacao compensacao'),
('A isenção por vendas mensais de ações também vale para day trade?','Não. Segundo a apostila (edição janeiro/2026), não há isenção de IR para day trade, mesmo quando o valor de vendas é inferior ao limite de operações comuns.','234','tributacao renda_variavel'),
])
add(14,[
('Como diferem classes abertas e fechadas de fundos?','Na classe aberta, o cotista pode pedir resgate conforme prazos do regulamento. Na classe fechada, em regra não há resgate a qualquer momento; a saída ocorre por amortização, liquidação ou negociação de cotas, conforme documentos.','241','fundos classes'),
('O que significa cota de abertura e cota de fechamento?','Cota de abertura usa patrimônio de referência no início do dia e é usada em fundos de baixa volatilidade conforme regras; cota de fechamento reflete valores apurados ao fim do dia e movimentos de mercado.','244','fundos cotas'),
('O que pode acontecer se o fundo fechar para resgates por falta de liquidez?','Em situações excepcionais, o administrador pode suspender resgates e adotar procedimentos previstos na regulamentação e no regulamento, comunicando os cotistas e protegendo tratamento equitativo.','245','fundos liquidez'),
('O que é fundo multimercado?','Classe que pode combinar diferentes fatores de risco e estratégias, como juros, câmbio e ações, conforme política e limites do regulamento. Maior flexibilidade também exige entender riscos e alavancagem.','246','fundos fif'),
('O que significa alavancagem em um fundo?','Assumir exposição ou risco superior ao patrimônio líquido do fundo, geralmente por derivativos; perdas podem ser ampliadas e exigir recursos adicionais conforme estrutura e limites.','258','fundos riscos'),
])
add(15,[
('O administrador de fundo pode garantir rentabilidade predeterminada?','Não. A apostila lista como vedado aos administradores e gestores garantir retornos predeterminados aos cotistas.','260','fundos participantes'),
('Qual é o principal dever do gestor quanto à carteira?','Decidir compra e venda de ativos e observar limites de composição, concentração e fatores de risco definidos para a classe.','261','fundos participantes'),
('Como marcação a mercado protege cotistas?','Registra ativos por preços correntes ou estimativas adequadas quando não há preço observável, refletindo variações na cota e reduzindo transferência de riqueza entre quem entra e sai.','270','fundos marcacao_mercado'),
('Qual é o quórum de instalação da assembleia de cotistas de fundos (Resolução CVM 175)?','A assembleia geral instala-se com qualquer número de cotistas presentes (art. 74 da Resolução CVM 175). A regra de 5% das cotas emitidas aplica-se à iniciativa para solicitar sua convocação, e não ao quórum de instalação (o trecho da apostila indica 5% para deliberação de forma imprecisa).','256','fundos assembleia'),
])
add(17,[
('Qual benefício fiscal o PGBL pode oferecer na fase de contribuição?','Segundo a apostila (edição janeiro/2026), contribuições ao PGBL podem ser deduzidas até 12% da renda bruta tributável anual, quando atendidos os requisitos da declaração completa e contribuição à previdência oficial.','307','previdencia pgbl tributacao'),
('Quando ocorre o fato gerador de IR em PGBL e VGBL?','Segundo a apostila (edição janeiro/2026), ocorre no resgate ou no recebimento do benefício. A base difere: saldo total no PGBL, rendimentos no VGBL.','309','previdencia tributacao'),
('Como a tabela regressiva de previdência muda com o prazo?','Segundo a apostila (edição janeiro/2026), a alíquota diminui conforme o tempo de permanência de cada contribuição, alcançando a menor faixa após prazo longo; a decisão é definitiva no regime regressivo.','310','previdencia regressivo'),
])
add(18,[
('Como funciona o rotativo do cartão de crédito?','É usado quando o cliente não paga o total da fatura; financia o saldo pendente e pode gerar juros elevados. A apostila descreve a migração para parcelamento após o período previsto.','316','credito cartao'),
('Como funciona o crédito consignado?','A parcela é descontada da remuneração ou benefício, respeitando margem consignável. No exemplo da apostila, 35% de renda líquida de R$4.200 corresponde a R$1.470.','318','credito consignado calculo'),
('O que caracteriza crédito direto ao consumidor (CDC)?','Financiamento destinado à compra de bens ou serviços, como veículos, com pagamento parcelado e garantia/condições previstas no contrato.','319','credito cdc'),
('Como leasing difere de financiamento tradicional?','No leasing, a instituição arrenda o bem ao cliente durante o contrato, com opção de compra ou outras alternativas no final; a propriedade jurídica permanece com arrendadora durante o arrendamento.','320','credito leasing'),
])

add(13,[
('Como calcular o custo médio de duas compras de ações?','Use a média ponderada: (quantidade 1×preço 1 + quantidade 2×preço 2)/(quantidade total). Exemplo: 100 a R$10 e 100 a R$12 dão custo médio de R$11 por ação.','230','tributacao custo_medio calculo'),
('Qual é a base tributável de uma venda de ações no mercado à vista?','Ganho líquido = valor de venda − custo médio de aquisição − despesas necessárias da operação. Perdas acumuladas elegíveis podem reduzir a base segundo as regras de compensação.','230','tributacao base_calculo'),
('O que é o “dedo-duro” nas operações comuns com ações?','Segundo a apostila (edição janeiro/2026), há IRRF de 0,005% sobre o valor da venda, retido pela intermediária e compensável com o imposto apurado sobre o lucro.','231','tributacao irrf'),
('Qual prazo a apostila dá para recolher via DARF o IR de operação comum?','Segundo a apostila (edição janeiro/2026), o contribuinte recolhe o imposto sobre o ganho líquido até o último dia útil do mês seguinte à operação.','231','tributacao darf'),
('Em uma venda por R$90.000, com custo de R$60.000, despesas de R$600 e prejuízo compensável de R$2.000, qual o IR de operação comum?','Ganho líquido = 90.000−60.000−600−2.000 = R$27.400. IR = 15%×27.400=R$4.110; IRRF compensável = 0,005%×90.000=R$4,50; saldo a recolher = R$4.105,50, segundo o exemplo da apostila (edição janeiro/2026).','231','tributacao calculo'),
('Como se calcula o imposto de day trade sobre lucro de R$6.000?','Segundo a apostila (edição janeiro/2026), IR total = 20%×6.000=R$1.200. A intermediária retém 1% do lucro (R$60) e o investidor recolhe R$1.140 via DARF até o último dia útil do mês seguinte.','233','tributacao day_trade calculo'),
('Qual critério define uma operação de day trade para a apostila?','A compra e a venda, ou combinação de operações, começa e termina no mesmo dia com o mesmo ativo, com liquidação total ou parcial da quantidade negociada.','233','tributacao day_trade'),
('Como compensar prejuízos de renda variável?','Segundo a apostila (edição janeiro/2026), prejuízo de operação comum compensa ganho comum; prejuízo de day trade compensa day trade. A compensação pode seguir para meses posteriores, mas não retroage para meses anteriores.','235','tributacao compensacao'),
('Quais segmentos de renda fixa o IMA-B 5 e o IMA-B 5+ representam?','O IMA-B 5 reúne títulos indexados ao IPCA com prazo de até 5 anos; IMA-B 5+ reúne títulos com prazo superior a 5 anos.','223','indices renda_fixa'),
('Como diferem Ibovespa e IBrX segundo a apostila?','Ambos acompanham carteiras teóricas de ações, mas usam critérios e ponderações diferentes; o Ibovespa pondera por negociabilidade e o IBrX por valor de mercado do free float, conforme metodologia descrita.','224','indices renda_variavel'),
('O que o IDIV procura representar?','Desempenho de ações de empresas que se destacam por remuneração aos acionistas, segundo os critérios metodológicos do índice.','225','indices renda_variavel'),
])
add(16,[
('Como se classificam fundos para tributação segundo o prazo médio da carteira?','Segundo a apostila (edição janeiro/2026), fundos de curto prazo têm carteira com prazo médio até 365 dias; fundos de longo prazo, superior a 365 dias; fundos de ações mantêm pelo menos 67% da carteira em ativos elegíveis de ações.','283','fundos tributacao'),
('Quais são as alíquotas de resgate de fundos de longo prazo?','Segundo a apostila (edição janeiro/2026): 22,5% até 180 dias; 20% de 181 a 360; 17,5% de 361 a 720; e 15% acima de 720 dias. Come-cotas antecipa 15% em maio e novembro.','284','fundos tributacao'),
('Quais alíquotas incidem sobre fundos de curto prazo?','Segundo a apostila (edição janeiro/2026), 22,5% até 180 dias e 20% a partir de 181 dias. O come-cotas antecipa 20% nos últimos dias úteis de maio e novembro.','284','fundos tributacao'),
('Há come-cotas em fundo de ações?','Não. Segundo a apostila (edição janeiro/2026), fundo de ações com pelo menos 67% de ativos elegíveis paga IR apenas no resgate, à alíquota de 15%, sem come-cotas.','286','fundos tributacao'),
('Como funciona o come-cotas no exemplo de fundo curto prazo?','Com rendimento de R$1.000 e IOF de R$460 a considerar, a base indicada fica em R$540; IR antecipado a 20% é R$108. Com cota de R$1,10, resgatam-se 98,1818 cotas para recolher o imposto.','285','fundos tributacao calculo'),
('Como compensar perdas entre fundos?','Segundo a apostila (edição janeiro/2026), perdas compensam rendimentos de fundos de mesma classificação tributária (curto, longo ou ações), sob o mesmo administrador; em conta e ordem, pode haver compensação pela mesma instituição intermediária conforme regras descritas.','287','fundos tributacao compensacao'),
('Quais requisitos a apostila lista para isenção de rendimentos de FII a pessoa física?','A apostila (edição janeiro/2026) lista negociação em bolsa ou balcão organizado, ao menos 100 cotistas e limite de participação individual. Correção pela Lei 11.033/2004, art. 3º, § 1º: as cotas devem ser admitidas à negociação exclusivamente nesses mercados; a pessoa física deve deter menos de 10% das cotas e não ter direito a mais de 10% dos rendimentos do fundo. Para pessoas físicas ligadas, o conjunto deve deter menos de 30% das cotas e não ter direito a mais de 30% dos rendimentos. A expressão da apostila “mais de 10% das cotas” é imprecisa: exatamente 10% já exclui a isenção. Referência complementar: <a href="https://www2.camara.leg.br/legin/fed/lei/2004/lei-11033-21-dezembro-2004-535177-normaatualizada-pl.html">Lei 11.033/2004, art. 3º</a>.','283','fii tributacao'),
('Quando ocorre o fato gerador de IR em fundos sujeitos a come-cotas?','Segundo a apostila (edição janeiro/2026), no último dia útil de maio e novembro, ou no resgate se ocorrer em outra data; a base considera a variação positiva da cota após IOF quando aplicável.','283','fundos tributacao'),
])
add(25,[
('Como calcular o índice de liquidez corrente pessoal?','Ativo circulante ÷ passivo circulante. Ele compara recursos e obrigações de curto prazo; maior tende a indicar melhor capacidade de pagamento, sem substituir avaliação de liquidez real.','383','indicadores liquidez'),
('Como calcular liquidez seca?','(Ativo circulante − estoques) ÷ passivo circulante. Exclui estoques da cobertura por serem menos líquidos.','383','indicadores liquidez'),
('Como calcular liquidez imediata?','Disponíveis ÷ passivo circulante. Considera caixa, conta e recursos de disponibilidade imediata.','383','indicadores liquidez'),
('Como calcular liquidez geral?','(Ativo circulante + realizável a longo prazo) ÷ (passivo circulante + passivo não circulante). Compara ativos realizáveis e obrigações de curto e longo prazo.','383','indicadores liquidez'),
('Como calcular cobertura de despesas mensais?','Reservas líquidas ÷ despesas mensais. Se há R$24.000 em ativos líquidos e despesas essenciais de R$6.000 por mês, cobertura = 4 meses.','383','indicadores cobertura'),
('Como calcular índice de endividamento sobre ativos?','Passivo total ÷ ativo total. Se passivos são R$180.000 e ativos R$450.000, índice = 40%; 60% corresponde a patrimônio líquido.','383','indicadores endividamento calculo'),
('Como calcular índice de poupança?','Sobra financeira ÷ receita. Se a renda líquida é R$8.000 e sobra R$1.200, poupança = 15% da renda.','383','indicadores poupanca calculo'),
('Como calcular dívida sobre patrimônio líquido?','Passivo total ÷ patrimônio líquido. Índice 1,0 indica passivos iguais ao patrimônio líquido; acima de 1,0, dívidas superam capital próprio.','380','indicadores endividamento'),
('Como calcular o coeficiente de investimento do patrimônio?','Ativos investidos ÷ total de ativos × 100. O resultado percentual mostra quanto dos ativos está aplicado em bens ou investimentos com capacidade de valorização ou geração de renda.','380','indicadores investimentos'),
('Como calcular o coeficiente de renda passiva?','Renda passiva ÷ renda total. Se investimentos geram R$2.000 e renda total é R$10.000 no mês, coeficiente = 20%.','382','indicadores renda_passiva'),
('Como calcular o custo médio da dívida?','Encargos financeiros e juros das dívidas ÷ saldo total das dívidas, usando o mesmo período. O indicador aproxima o peso do crédito sobre o orçamento.','382','indicadores custo_divida'),
])

add(21,[
('O que é um arranjo de pagamento?','Conjunto de regras e procedimentos que organiza como recursos passam do pagador ao recebedor e define participantes, fluxos e padrões de segurança.','452','servicos_bancarios pagamentos'),
('Que etapas o adquirente executa em uma compra com cartão?','Credencia o estabelecimento, captura e processa a transação junto ao emissor e participa da liquidação do valor ao lojista.','453','servicos_bancarios pagamentos'),
('Quando um pequeno comércio pode usar um subadquirente?','Quando precisa aceitar pagamentos eletrônicos por uma plataforma simplificada; o subadquirente conecta o comerciante ao adquirente e demais participantes do arranjo.','454','servicos_bancarios pagamentos'),
('Como diferem depósito à vista e depósito a prazo?','Depósito à vista pode ser movimentado a qualquer momento; depósito a prazo é aplicado por condições e vencimento pactuados, podendo haver restrição de resgate antecipado.','335','servicos_bancarios depositos'),
('Para que serve um boleto bancário?','É instrumento de cobrança e pagamento que pode ser quitado em bancos, aplicativos ou correspondentes, conforme os canais disponíveis.','336','servicos_bancarios boleto'),
])
add(22,[
('Qual é a diferença entre risco puro e risco especulativo em seguros?','Risco puro envolve possibilidade de perda, sem oportunidade de ganho, como colisão de automóvel. Risco especulativo pode resultar em ganho ou perda, como investimento em ações.','337','seguros riscos'),
('O que a apólice registra?','Formaliza o contrato, descrevendo direitos e obrigações de seguradora e segurado e discriminando as garantias contratadas.','337','seguros contrato'),
('O que é endosso em um seguro?','Documento que altera característica ou dado do contrato original, como endereço, veículo ou inclusão de beneficiário.','337','seguros contrato'),
('Qual é a diferença entre cobertura básica e adicional?','A cobertura básica é a principal e obrigatória para emissão da apólice. Coberturas adicionais são opcionais, cobrem riscos fora da básica e podem exigir prêmio extra.','338','seguros cobertura'),
('O que significa carência no seguro?','Período entre contratação e início da cobertura durante o qual a seguradora não responde por sinistros conforme as condições do contrato.','338','seguros carencia'),
('Qual é a diferença entre resseguro e cosseguro?','Resseguro transfere parte do risco da seguradora para outra entidade. No cosseguro, duas ou mais seguradoras dividem o mesmo contrato e o risco desde a origem.','339','seguros resseguro cosseguro'),
('Qual é a diferença entre seguro de vida temporário e vitalício?','Temporário cobre prazo definido e não paga benefício se o evento não ocorrer no período. Vitalício mantém cobertura por toda a vida, conforme condições contratuais.','340','seguros vida'),
('O seguro residencial cobre automaticamente todos os danos?','Não. A cobertura básica indicada é incêndio, raio e explosão. Vendaval, granizo, alagamento e danos elétricos podem exigir cobertura adicional; consulte a apólice.','341','seguros residencial'),
('Como funciona o bônus do seguro automóvel?','A cada ano sem sinistro o segurado pode receber desconto; um sinistro pode reduzir bônus. A apostila ressalta que serviços como guincho não entram nessa contagem.','341','seguros automovel'),
])
add(24,[
('Qual tamanho de reserva de emergência costuma ser adequado para a maioria das pessoas?','A apostila sugere de três a seis meses de despesas essenciais; renda instável e maiores responsabilidades podem exigir reserva maior.','368','reserva_emergencia'),
('Qual é o valor de uma reserva de seis meses para despesas essenciais de R$4.600 mensais?','R$4.600×6 = R$27.600. Para três meses, o mínimo ilustrativo da apostila seria R$13.800.','369','reserva_emergencia calculo'),
('Que reserva a apostila sugere para renda instável ou dependentes?','Como referência: 6 meses para assalariados estáveis sem dependentes e alta empregabilidade; 12 meses para autônomos, renda variável ou dependentes; 18 meses para único provedor ou baixa empregabilidade.','371','reserva_emergencia'),
('Onde manter a reserva de emergência?','Em instrumentos de alta liquidez, baixo risco e acesso imediato, como CDB de liquidez diária com garantia elegível ou conta remunerada protegida; evite ativos voláteis e ilíquidos.','371','reserva_emergencia'),
('Por que o tamanho da reserva depende do capital humano?','Estabilidade profissional, previsibilidade de renda e facilidade de recolocação mudam o tempo provável sem renda; renda variável e dependentes favorecem uma reserva maior.','370','reserva_emergencia'),
])

add(11,[
('Como diferem COE com valor nominal protegido e COE com valor nominal em risco?','No valor nominal protegido, o pagamento mínimo busca devolver ao menos o capital inicial no vencimento, sujeito ao risco do emissor. No valor nominal em risco, o investidor pode receber menos que o valor aplicado, conforme o cenário.','187','coe estruturas'),
])
add(26,[
('Quais são as três categorias de rendimentos no IRPF apresentadas pela apostila?','Regime tributável, regime definitivo ou exclusivo na fonte e rendimentos isentos. A classificação determina se o valor compõe a base anual, se o imposto já é definitivo ou se não há incidência.','388','irpf classificacao'),
('Como é calculado ganho de capital na venda de um bem?','Valor de alienação menos custo de aquisição. Exemplo: compra por R$200 mil e venda por R$500 mil gera ganho bruto de R$300 mil antes de despesas, isenções ou regras de apuração.','387','irpf ganho_capital calculo'),
('Qual parcela de renda bruta tributável a apostila admite deduzir em PGBL?','Segundo a apostila (edição janeiro/2026), até 12%, quando aplicáveis os requisitos fiscais. Essa dedução não significa isenção definitiva; o saldo do PGBL é tributado no resgate/benefício.','390','irpf previdencia'),
])

# Validate references against extracted page split and printed footer numbers.
pages=Path('flashcards/cpa/fontes/apostila_cpa.txt').read_text(encoding='utf-8').split('\f')
for n,q,a,p,t in C:
 page_list=[int(v.strip()) for v in p.split(',')]; assert all(v<=len(pages) and pages[v-1].strip() for v in page_list), (q,p)
 for page in page_list: assert re.search(rf'(?m)^\s*{page}\s*$',pages[page-1]), ('footer',p,q)
# unique fronts and no empty content
assert len({x[1] for x in C})==len(C)
for n in [3,4,5,6,7,*range(9,19),*range(21,30),31,32,33]: assert any(x[0]==n for x in C), n
# Emit one unique consolidated set and per-topic decks.
def build(rows,path,delimiter='\t'):
 with path.open('w',encoding='utf-8',newline='') as f:
  separator='Tab' if delimiter=='\t' else 'Comma'
  f.write(f'#separator:{separator}\n#html:true\n#tags column:3\n')
  topics={row[0] for row in rows}
  if len(topics)==1:
   f.write(f'#deck:{deck_names[next(iter(topics))]}\n')
  f.write('#deck column:4\n')
  w=csv.writer(f,delimiter=delimiter,lineterminator='\n',quoting=csv.QUOTE_MINIMAL)
  w.writerow(['#columns:Frente','Verso','Tags','Deck'])
  for n,q,a,p,t in rows:
   # PDF and printed pagination match in all cited content pages.
   pdf_ref=' e '.join(p.split(','))
   print_ref=' e '.join(p.split(','))
   ref=f'<br><small>Fonte: Apostila CPA, ed. janeiro/2026, p. impressa {print_ref} (PDF {pdf_ref}).</small>'
   tags=' '.join(['cpa::apostila',f'cpa::{n:02d}',*[f'tema::{x}' for x in t.split()]])
   w.writerow([q,a+ref,tags,deck_names[n]])
ROOT.mkdir(parents=True,exist_ok=True)
for n in sorted({x[0] for x in C}):
 build([x for x in C if x[0]==n],DECK_ROOT/f'cpa_{n:02d}.tsv')
build(C,DECK_ROOT/'cpa_apostila_completo.tsv')
# Coverage mapping, taking every scheduled task title and description from the source plan.
topic_dir=DECK_ROOT
topic_dir.mkdir(exist_ok=True)
topic_files=[]
for item in plan:
 n=int(re.search(r'CPA\s+(\d+)',item['titulo']).group(1))
 cards=[x for x in C if x[0]==n]
 if not cards: continue
 title=re.split(r'\s+—\s+',item['titulo'],maxsplit=1)[1].replace('/',' e ')
 portable_title=re.sub(r'[<>:"\\|?*]', ' - ', title).rstrip(' .')
 filename=f'{n:02d} - {portable_title}.csv'
 build(cards,topic_dir/filename,delimiter=',')
 topic_files.append((filename,len(cards)))
with (topic_dir/'INDICE.md').open('w',encoding='utf-8') as f:
 f.write('# CPA por tema\n\nArquivos CSV em ordem numérica do planejamento. Cada arquivo contém Frente, Verso, Tags e Deck. A coluna Deck cria os subdecks dentro de CPA automaticamente ao importar novos cartões no Anki.\n\n')
 for filename,count in topic_files:
  f.write(f'- [{filename}](<{filename}>): {count} cartões.\n')
 f.write('\nImporte estes CSVs ou o consolidado desta pasta. Os dois contêm os mesmos cartões. As tarefas de revisão e simulado estão mapeadas em `apostila/cobertura.csv`.\n')
review_tags={8:['cpa::01','cpa::02','cpa::03','cpa::04','cpa::05','cpa::06','cpa::07'],19:['cpa::09','cpa::10','cpa::11','cpa::14','cpa::15','cpa::16'],20:['cpa::12','cpa::13','cpa::17','cpa::18'],30:['cpa::23','cpa::24','cpa::25','cpa::26','cpa::27','cpa::28','cpa::29'],39:['cpa::01','cpa::02','cpa::03','cpa::04','cpa::05','cpa::06','cpa::07','cpa::09','cpa::10','cpa::11','cpa::12','cpa::13','cpa::14','cpa::15','cpa::16','cpa::17','cpa::18','cpa::21','cpa::22','cpa::23','cpa::24','cpa::25','cpa::26','cpa::27','cpa::28','cpa::29','cpa::31','cpa::32','cpa::33']}
rows=[]
for ix,item in enumerate(plan):
 n=int(re.search(r'CPA\s+(\d+)',item['titulo']).group(1)); title=item['titulo']; desc=item['descricao']
 if n==22:
  tags=['cpa::22']
  selection='cpa::22 (seguros); revisão: cpa::09 a cpa::18 e cpa::21'
  deck='cpa_22.tsv + seleção de revisão dos decks CPA09–18 e CPA21'
  status='Conteúdo novo no deck CPA22 e revisão por tags; não duplicar notas.'
 elif n in review_tags:
  tags=review_tags[n]
  selection='; '.join(tags)
  deck='Seleção nos decks temáticos: '+', '.join(({1:'01_sfn_orgaos.txt',2:'02_participantes_spb_pagamentos.txt'}.get(int(tag[-2:])) or f'cpa_{int(tag[-2:]):02d}.tsv') for tag in tags)
  status='Seleção dos cartões existentes por tags; sem cartões de revisão artificiais.'
  if n==39: status='Revisão cumulativa opcional por tags e erros pessoais; adapte à data real da prova.'
 elif n in [34,36,38]:
  selection='Simulado completo da plataforma ou bateria externa; questões não fornecidas neste trabalho.'
  deck='Sem deck novo. Use coleção apenas como revisão posterior.'
  status='Depende de material/respostas pessoais ainda não fornecidos. Anki não substitui simulado.'
 elif n in [35,37]:
  selection='Para cada erro ou acerto por dúvida, localizar o tema na apostila e associar à tag tema::*; criar cartão próprio com explicação do erro.'
  deck='Coleção pertinente + cartões pessoais pós-correção.'
  status='Depende dos itens e justificativas dos simulados pessoais, ainda não fornecidos.'
 else:
  deck=f'cpa_{n:02d}.tsv'
  selection='Ver inventario_subtopicos.csv pelas tags do tópico.'
  status='Deck teórico criado; confira o inventário para subtópicos e cartões vinculados.'
 rows.append([f'CPA {n:02d}',title,desc,deck,status,selection])
with (ROOT/'cobertura.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f,lineterminator="\n"); w.writerow(['Tarefa','Título do CSV','Descrição do CSV','Deck/seleção','Situação e limite','Cobertura/procedimento']); w.writerows(rows)
# Inventory joins every study subtopic tag to its unique card IDs and prompts.
inv={}
for idx,(n,q,a,p,t) in enumerate(C,1):
 for theme in t.split(): inv.setdefault((n,theme),[]).append((idx,q,p))
with (ROOT/'inventario_subtopicos.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f,lineterminator="\n"); w.writerow(['Tarefa','Tag de conteúdo','Quantidade de cartões','IDs/cartões vinculados'])
 for (n,theme),items in sorted(inv.items()):
  w.writerow([f'CPA {n:02d}',f'tema::{theme}',len(items),'; '.join(f'N{i:03d} {q} (p. {p})' for i,q,p in items)])
print('cards',len(C),'topics',len({x[0] for x in C}))
