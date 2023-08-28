from iOS.IBS.Control.onboarding_Control_iRD import Onboarding
from iOS.IBS.Control.questionnaire_Control_iRD import Questionnaire

onboard = Onboarding()
onboard.test_setup()
onboard.test_onboarding()
onboard.test_teardown()

questionnaire = Questionnaire()
questionnaire.test_setup()
questionnaire.test_questionnaire()
questionnaire.test_teardown()
