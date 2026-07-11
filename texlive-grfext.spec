%global tl_name grfext
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Manipulate the graphics packages list of extensions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/grfext
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grfext.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grfext.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grfext.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides macros for adding to, and reordering the list of
graphics file extensions recognised by package graphics.

