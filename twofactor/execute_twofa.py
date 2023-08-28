# from androidRealDevice.IBS.Intervention.questionnaire_IBS_Intervention import Questionnaire
# from twofactor.onboard_control_2FA import Onboarding
# from twofactor.onboard_Int_2FA import Onboarding
# from twofactor.onboard_DiGA_2FA import Onboarding
# from twofactor.onboard_HB_2FA import Onboarding
from twofactor.onboard_DocIBS import Onboarding
# from twofactor.onboard_IBD_Rem_2FA import Onboarding

onboard = Onboarding()
onboard.test_setup()
onboard.test_onboarding()
onboard.test_teardown()

# questionnaire = Questionnaire()
# questionnaire.test_setup()
# questionnaire.test_ques()
# questionnaire.test_teardown()
