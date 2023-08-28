from androidRealDevice.IBS.Doc_IBS.articles_DocIBS import Articles
from androidRealDevice.IBS.Doc_IBS.questionnaire_DocIBS import Questionnaire
from androidRealDevice.IBS.Doc_IBS.onboarding_DocIBS import Onboarding

onboard = Onboarding()
onboard.test_setup()
onboard.test_onboarding()
onboard.test_teardown()

articles = Articles()
articles.setup()
articles.testarticles()
articles.teardown()

questionnaire = Questionnaire()
questionnaire.testquestionnaire()
