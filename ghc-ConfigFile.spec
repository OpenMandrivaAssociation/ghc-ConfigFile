%global debug_package %{nil}

%define module ConfigFile

Summary:	Configuration file reading & writing
Name:		ghc-%{module}
Version:	1.1.1
Release:	3
License:	LGPLv2+
Group:		Development/Other
Url:		http://hackage.haskell.org/package/%{module}
Source0:	http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
Source10:	%{name}.rpmlintrc
BuildRequires:	ghc-devel
BuildRequires:	haddock
BuildRequires:	haskell-macros
BuildRequires:	haskell(MissingH)
BuildRequires:	haskell(parsec)
Requires(post,preun):	ghc
Requires(pre):	haskell(MissingH)
Requires(pre):	haskell(mtl)
Requires(pre):	haskell(parsec)

%description
Parser and writer for handling sectioned config files in Haskell.

The ConfigFile module works with configuration files in a standard
format that is easy for the user to edit, easy for the programmer
to work with, yet remains powerful and flexible. It is inspired by,
and compatible with, Python's ConfigParser module. It uses files
that resemble Windows .INI-style files, but with numerous
improvements.

ConfigFile provides simple calls to both read and write config files.
It's possible to make a config file parsable by this module,
the Unix shell, and make.

%files
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%{_cabal_rpm_deps_dir}
%{_cabal_haddoc_files}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

