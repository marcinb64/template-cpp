#include "core/core.h"

#include <spdlog/spdlog.h>

/* -------------------------------------------------------------------------- */

int main()
{
    spdlog::set_level(spdlog::level::debug);

    try {
        spdlog::debug("hello {}!", getRandomNumber());
    }

    catch (std::exception &e) {
        spdlog::critical(e.what());
    }

    return 0;
}
