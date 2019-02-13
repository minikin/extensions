require 'fileutils'
require 'pathname'
require 'benchmark'

BUILD_DIR = Pathname.new("build")

# Set to true if you want to run tests with extensions
USE_EXTENSIONS = true

num_tests = 1000

general_list = [100, 1000, 2000, 3000, 5000, 10000]
apps_list = [0, 46, 144, 155, 182, 280, 381, 388]

desc "Generate temporary files"
task :generate do
  Rake::Task['clean'].execute
  FileUtils.mkdir_p BUILD_DIR
  methods = USE_EXTENSIONS ? 1 : num_tests
  extensions = USE_EXTENSIONS ? num_tests : 0
  method_body = "for item in 0..<n { let newItem = item + 2; print(newItem)}"
  File.open(BUILD_DIR + "main.swift", 'w') do |f|
    f.puts "class MyClass {"
    f.puts "let n = 1000"
    1.upto(methods) do |idx|
      f.puts "func method_#{idx}() { "
      f.puts method_body
      f.puts "}"
    end
    f.puts "}"
    f.puts
    1.upto(extensions) do |idx|
      f.puts "extension MyClass {"
      f.puts "func method_ext_#{idx}() {"
      f.puts method_body
      f.puts "}"
      f.puts "}"
    end
  end
end

desc "Run single compilation cycle"
task :compile do
  system("swiftc -Onone #{BUILD_DIR}/*.swift")
end

desc "Run multiple compilation cycle"
task :benchmark do
  apps_list.each do |tests|
    num_tests = tests
    puts "Using #{num_tests} #{USE_EXTENSIONS ? 'extensions' : 'methods'}"
    puts "========================================="
    avg = 0
    num_runs = 10
    1.upto(num_runs) do |idx|
      Benchmark.bm do |b|
        Rake::Task["generate"].execute
        t = b.report("compile: ") { Rake::Task["compile"].execute }
        avg += t.total / num_runs
      end
    end
    puts "========================================="
    puts "Average compile time for n=#{tests} is #{avg.round(4)}"
    puts "========================================="
  end
end

task :clean do
  FileUtils.rm_rf BUILD_DIR
  FileUtils.rm_rf "test"
  FileUtils.rm_rf "main"
end

