Name:		python-ajsonrpc
Version:	1.2.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/a/ajsonrpc/ajsonrpc-%{version}.tar.gz
Summary:	Async JSON-RPC 2.0 protocol + server powered by asyncio
URL:		https://pypi.org/project/ajsonrpc/
License:	MIT
Group:		Development/Python

Requires:   python%{pyver}dist(setuptools)

BuildSystem:	python

BuildArch:	noarch

%description
Async JSON-RPC 2.0 protocol + server powered by asyncio

%files
%{py_sitedir}/ajsonrpc
%{py_sitedir}/ajsonrpc-*.*-info
%{_bindir}/async-json-rpc-server
