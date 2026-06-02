1. Running Rust
	- rustc main.rs - Compile a Rust source file into a binary.
	- rustc main.rs -o app - Compile and write the output binary as app.
	- ./main - Run the compiled binary in the current directory.
	- cargo run - Build and run the current Cargo project.
	- cargo run --release - Build and run the optimized release build.
	- rustc --version - Show the installed Rust compiler version.
	- cargo --version - Show the installed Cargo version.
	- which rustc - Show the path to the Rust compiler.
	- which cargo - Show the path to Cargo.

2. Crates & Dependencies
	- cargo search <crate> - Search crates.io for a crate.
	- cargo add <crate> - Add a dependency to Cargo.toml.
	- cargo add <crate> --dev - Add a development-only dependency.
	- cargo remove <crate> - Remove a dependency from Cargo.toml.
	- cargo update - Update dependencies in Cargo.lock.
	- cargo tree - Show the dependency tree for the project.
	- cargo metadata - Print project metadata as JSON.

3. Builds & Checks
	- cargo build - Build the current project.
	- cargo build --release - Build an optimized release version.
	- cargo check - Type-check the project without producing a final binary.
	- cargo check --workspace - Check all packages in a workspace.
	- cargo build --target <triple> - Build for a specific compilation target.
	- cargo clean - Remove build artifacts from the target directory.

4. Toolchains & rustup
	- rustup --version - Show the installed rustup version.
	- rustup show - Show installed toolchains and the active default.
	- rustup update - Update Rust toolchains and related tools.
	- rustup default stable - Set the default toolchain to stable.
	- rustup toolchain list - List installed Rust toolchains.
	- rustup target list --installed - List installed compilation targets.
	- rustup target add wasm32-unknown-unknown - Add a compilation target.
	- rustup component add rustfmt - Install the rustfmt formatter.
	- rustup component add clippy - Install the Clippy linter.
	- rustup doc - Open local Rust documentation.

5. Formatting, Lints & Fixes
	- cargo fmt - Format the project with rustfmt.
	- cargo fmt --check - Check formatting without changing files.
	- cargo clippy - Run Clippy lints on the project.
	- cargo clippy -- -D warnings - Treat Clippy warnings as errors.
	- cargo fix - Apply compiler-suggested fixes where possible.
	- cargo fix --allow-dirty - Apply fixes even with uncommitted changes.

6. Testing & Docs
	- cargo test - Run the project's test suite.
	- cargo test <name> - Run tests matching a specific name.
	- cargo test -- --nocapture - Show test output printed to stdout.
	- cargo test --doc - Run documentation tests.
	- cargo doc --open - Build docs and open them in a browser.
	- cargo bench - Run benchmarks for the project.

7. Projects, Files & Modules
	- cargo new my_app - Create a new Rust binary project.
	- cargo new my_lib --lib - Create a new Rust library project.
	- cargo init - Initialize a Cargo project in the current directory.
	- cargo init --lib - Initialize the current directory as a library crate.
	- cargo run --example <name> - Run an example from the examples directory.
	- cargo run --bin <name> - Run a specific binary target in a workspace or multi-bin project.
	- cargo build -p <crate> - Build one package inside a workspace.
	- cargo test -p <crate> - Test one package inside a workspace.

8. Installing & Publishing
	- cargo install <crate> - Install a Cargo binary crate globally.
	- cargo install --path . - Install the current project as a binary.
	- cargo login <token> - Save your crates.io API token locally.
	- cargo package - Create a distributable crate package.
	- cargo publish - Publish the crate to crates.io.