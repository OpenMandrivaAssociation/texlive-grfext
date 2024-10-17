Name:		texlive-grfext
Version:	53024
Release:	2
Summary:	Manipulate the graphics package's list of extensions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/grfext
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grfext.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grfext.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grfext.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides macros for adding to, and reordering the
list of graphics file extensions recognised by package
graphics.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/grfext
%{_texmfdistdir}/tex/latex/grfext
%doc %{_texmfdistdir}/doc/latex/grfext

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
