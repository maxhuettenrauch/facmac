from facmac.learners.cq_learner import CQLearner
from facmac.learners.facmac_learner import FACMACLearner
from facmac.learners.facmac_learner_discrete import FACMACDiscreteLearner
from facmac.learners.maddpg_learner import MADDPGLearner
from facmac.learners.maddpg_learner_discrete import MADDPGDiscreteLearner

REGISTRY = {}
REGISTRY["cq_learner"] = CQLearner
REGISTRY["facmac_learner"] = FACMACLearner
REGISTRY["facmac_learner_discrete"] = FACMACDiscreteLearner
REGISTRY["maddpg_learner"] = MADDPGLearner
REGISTRY["maddpg_learner_discrete"] = MADDPGDiscreteLearner