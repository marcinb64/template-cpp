#include <core.h>

#include <catch2/catch_test_macros.hpp>
#include <catch2/catch_approx.hpp>

TEST_CASE("example", "[core]")
{
    CHECK(getRandomNumber() == 4);
}
