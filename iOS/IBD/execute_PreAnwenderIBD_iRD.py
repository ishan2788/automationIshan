from iOS.IBD.questionnaire_PreAnwenderIBD_iRD import Questionnaire
from iOS.IBD.onboarding_PreAnwenderIBD_iRD import Onboarding
from iOS.IBS.articles_iRD import Articles

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
