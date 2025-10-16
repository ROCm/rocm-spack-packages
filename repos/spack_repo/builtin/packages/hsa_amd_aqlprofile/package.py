# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class HsaAmdAqlprofile(CMakePackage):
    """Architected Queuing Language Profiling Library
    AQLprofile is an open source library that enables advanced
    GPU profiling and tracing on AMD platforms"""

    homepage = "https://github.com/ROCm/aqlprofile"
    git = "https://github.com/ROCm/rocm-systems.git"
    url = "https://github.com/ROCm/aqlprofile/archive/refs/tags/rocm-7.0.0.tar.gz"
    tags = ["rocm"]

    maintainers("srekolam", "renjithravindrankannath", "afzpatel")

    version("develop", commit="538ebc5409e139d0c4c4e9b86c284f98ff488990")
    version("7.0.0", sha256="25f040c867e22f4a0b4147317133dc50eccf60e72fc2c91e8d25083fa84c313e")

    for ver in ["7.0.0", "develop"]:
        depends_on(f"hsa-rocr-dev@{ver}", when=f"@{ver}")

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@develop"):
            return "projects/aqlprofile"
        else:
            return "."
