Name:		texlive-circuit-macros
Version:	65149
Release:	2
Summary:	M4 macros for electric circuit diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/circuit-macros
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/circuit-macros.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/circuit-macros.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of m4 macros for drawing high-quality electric circuits
containing fundamental elements, amplifiers, transistors, and
basic logic gates to include in TeX, LaTeX, or similar
documents. Some tools and examples for other types of diagrams
are also included. The macros can be evaluated to drawing
commands in the pic language, which is very easy to understand
and which has a good power/complexity ratio. Pic contains
elements of a simple programming language, and is well-suited
to line drawings requiring parametric or conditional
components, fine tuning, significant geometric calculations or
repetition, or that are naturally block structured or tree
structured. (The m4 and pic processors are readily available
for Unix and PC machines.) Alternative output macros can create
TeX output to be read by pstricks, TikZ commands for use by the
pgf bundle, or SVG.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/circuit-macros
%doc %{_texmfdistdir}/doc/latex/circuit-macros

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
