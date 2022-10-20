REGISTRY = {}

from facmac.runners.episode_runner import EpisodeRunner
REGISTRY["episode"] = EpisodeRunner

from facmac.runners.parallel_runner import ParallelRunner
REGISTRY["parallel"] = ParallelRunner
