FROM centos:7
MAINTAINER Hiroaki Nakamura <hnakamur@gmail.com>

RUN yum -y install rpmdevtools rpm-build \
 && rpmdev-setuptree

RUN yum -y install epel-release \
 && yum -y install python-pip \
 && pip install copr-cli

ADD highway.spec /root/rpmbuild/SPECS/

RUN version=`awk '$1=="Version:" {print $2}' /root/rpmbuild/SPECS/highway.spec` \
 && curl -sL -o /root/rpmbuild/SOURCES/v${version}.tar.gz https://github.com/tkengo/highway/archive/v${version}.tar.gz \
 && rpmbuild -bs /root/rpmbuild/SPECS/highway.spec

ADD copr-build.sh /root/
ENTRYPOINT ["/bin/bash", "/root/copr-build.sh"]
