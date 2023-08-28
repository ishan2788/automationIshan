from iOS.IBS.Doc_IBS.onboarding_docIBS_iRD import Onboarding
from iOS.IBS.articles_iRD import Articles
from iOS.IBS.Doc_IBS.questionnaire_docIBS_iRD import Questionnaire

onboarding = Onboarding()
onboarding.test_setup()
onboarding.test_onboarding()
onboarding.test_teardown()

articles = Articles()
articles.setup()
articles.testarticles()
articles.teardown()

questionnaire = Questionnaire()
questionnaire.test_setup()
questionnaire.test_questionnaire()
questionnaire.test_teardown()
