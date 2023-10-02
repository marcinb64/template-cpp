#include <somelib.h>

#include <catch2/catch_test_macros.hpp>

TEST_CASE("dummy")
{
    REQUIRE(somelib::foo(1) == 2);
}
